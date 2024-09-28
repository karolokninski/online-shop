import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from typing import List, Optional
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
DATABASE_URL = f"postgresql+asyncpg://shop:{POSTGRES_PASSWORD}@dpg-crnistt6l47c73ah51og-a.frankfurt-postgres.render.com:{POSTGRES_PORT}/shop_57s3"

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class EmailPasswordForm(BaseModel):
    email: str
    password: str

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float

    class Config:
        orm_mode = True

class OAuth2EmailPasswordRequestForm:
    def __init__(self, email: str = Form(), password: str = Form()):
        self.email = email
        self.password = password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def send_email(request_data):
    recipient_email = request_data["email"]
    subject = "Reset hasła"
    body_html = """\
        <html>
        <body>
            <p>
                Witaj!
            </p>
        </body>
        </html>
    """

    msg = MIMEMultipart()
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html"))

    try:
        server = smtplib.SMTP_SSL(
            os.getenv("EMAIL_SMTP_SERVER"), os.getenv("EMAIL_SMTP_PORT")
        )
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PWD"))
        server.sendmail(os.getenv("EMAIL_USER"), recipient_email, msg.as_string())
        server.quit()

    except Exception as error:
        print(error)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE username = :username OR email = :email"), {"username": user.username, "email": user.email})
    existing_user = query.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Konto o podanym adresie e-mail już istnieje.")

    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return {"username": db_user.username, "email": db_user.email}

@app.post("/token")
async def login_for_access_token(form_data: OAuth2EmailPasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE email = :email"), {"email": form_data.email})
    user = query.fetchone()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Nieprawidłowy adres e-mail lub hasło.")

    access_token = create_access_token(data={"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

@app.get("/products/", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM products LIMIT :limit OFFSET :skip"), {"limit": limit, "skip": skip})
    products = result.fetchall()
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM products WHERE id = :id"), {"id": product_id})
    product = result.fetchone()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM products WHERE id = :id"), {"id": product_id})
    db_product = result.fetchone()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    await db.execute(
        text("UPDATE products SET name = :name, description = :description, price = :price WHERE id = :id"), 
        {"name": product.name, "description": product.description, "price": product.price, "id": product_id}
    )
    await db.commit()

    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM products WHERE id = :id"), {"id": product_id})
    db_product = result.fetchone()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.execute(text("DELETE FROM products WHERE id = :id"), {"id": product_id})
    await db.commit()
    return {"message": "Product deleted successfully"}
