import os
import base64
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Form, Request, Query
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, Field, validator, EmailStr, constr
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Float, Text, select, text, DECIMAL, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, relationship, joinedload, selectinload
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY, BYTEA
from datetime import datetime, timedelta
from typing import List, Optional
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
from httpx import AsyncClient

load_dotenv()

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
EMAIL_SMTP_PORT = os.getenv("EMAIL_SMTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
CLIENT_ID = os.getenv("TPAY_CLIENT_ID", "your_client_id_here")
CLIENT_SECRET = os.getenv("TPAY_CLIENT_SECRET", "your_client_secret_here")
TPAY_AUTH_URL = os.getenv("TPAY_AUTH_URL", "https://api.tpay.com/oauth/auth")
TPAY_TRANSACTION_URL = os.getenv("TPAY_TRANSACTION_URL", "https://api.tpay.com/transactions")

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(100), nullable=False)
    parent_category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=True)
    description = Column(Text, nullable=True)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(150), nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    description = Column(Text, nullable=True)
    main_image = Column(BYTEA, nullable=True)
    additional_images = Column(ARRAY(BYTEA), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    category = relationship("ProductCategory")

class ProductParameter(Base):
    __tablename__ = 'product_parameters'
    id = Column(Integer, primary_key=True, index=True)
    parameter_name = Column(String(100), unique=True, nullable=False)

class ParameterValue(Base):
    __tablename__ = 'parameter_values'
    id = Column(Integer, primary_key=True, index=True)
    parameter_id = Column(Integer, ForeignKey('product_parameters.id', ondelete='CASCADE'))
    value = Column(Text, nullable=False)
    product_parameter_values = relationship("ProductParameterValue", back_populates="parameter_value")

class ProductParameterValue(Base):
    __tablename__ = 'product_parameter_values'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
    parameter_value_id = Column(Integer, ForeignKey('parameter_values.id', ondelete='CASCADE'))
    parameter_value = relationship("ParameterValue", back_populates="product_parameter_values")

class DeliveryMethod(Base):
    __tablename__ = 'delivery_methods'
    id = Column(Integer, primary_key=True, index=True)
    method_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    estimated_delivery_days = Column(Integer, nullable=True)
    cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)

class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    id = Column(Integer, primary_key=True, index=True)
    method_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    fee = Column(DECIMAL(10, 2), nullable=False, default=0.00)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, index=True)
    address_line = Column(String(255), nullable=False)
    postal_code = Column(String(20), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    hashed_password = Column(String(100), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id', ondelete="SET NULL"), nullable=True) 
    role = Column(String(20), default='user', nullable=False)
    note = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    address = relationship("Address", backref="users", uselist=False)
    

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    order_date = Column(TIMESTAMP, default=datetime.utcnow)
    delivery_method_id = Column(Integer, ForeignKey('delivery_methods.id', ondelete="SET NULL"))
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id', ondelete="SET NULL"))
    address_id = Column(Integer, ForeignKey('addresses.id', ondelete="SET NULL"))
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    order_status = Column(String(50), default='Pending')
    order_items = relationship("OrderItem", back_populates="order")
    address = relationship("Address")

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey('products.id', ondelete="SET NULL"))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    order = relationship("Order", back_populates="order_items")

class UserRegisterCreate(BaseModel):
    name: str
    email: str
    password: str

class EmailPasswordForm(BaseModel):
    email: str
    password: str

class ProductCategoryCreate(BaseModel):
    category_name: str
    parent_category_id: Optional[int] = None
    description: Optional[str] = None

class ProductCategoryResponse(BaseModel):
    id: int
    category_name: str
    parent_category_id: Optional[int] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    product_name: str
    category_id: Optional[int] = None
    price: float
    stock_quantity: Optional[int] = 0
    description: Optional[str] = None
    main_image: Optional[str] = None
    additional_images: Optional[List[str]] = None

    @validator('main_image', pre=True, always=True)
    def validate_main_image(cls, v):
        if v is not None:
            try:
                base64.b64decode(v)
            except (ValueError, TypeError):
                raise ValueError("main_image must be a valid Base64 encoded string")
        return v

    @validator('additional_images', each_item=True, pre=True, always=True)
    def validate_additional_images(cls, v):
        if v is not None:
            try:
                base64.b64decode(v)
            except (ValueError, TypeError):
                raise ValueError("Each item in additional_images must be a valid Base64 encoded string")
        return v

class ProductResponse(BaseModel):
    id: int
    product_name: str
    category_id: Optional[int]
    price: float
    stock_quantity: int
    description: Optional[str]
    main_image: Optional[str]
    additional_images: Optional[List[str]]
    created_at: datetime

    class Config:
        from_attributes = True

        json_encoders = {
            bytes: lambda v: encode_to_base64(v)
        }

    @classmethod
    def from_orm(cls, obj):
        additional_images_base64 = [encode_to_base64(img) for img in obj.additional_images or []]
        return cls(
            id=obj.id,
            product_name=obj.product_name,
            category_id=obj.category_id,
            price=obj.price,
            stock_quantity=obj.stock_quantity,
            description=obj.description,
            main_image=encode_to_base64(obj.main_image),
            additional_images=additional_images_base64,
            created_at=obj.created_at,
        )

class ProductParameterCreate(BaseModel):
    parameter_name: str

class ProductParameterResponse(ProductParameterCreate):
    id: int

    class Config:
        from_attributes = True

class ParameterValueCreate(BaseModel):
    parameter_id: int
    value: str

class ParameterValueResponse(ParameterValueCreate):
    id: int

    class Config:
        from_attributes = True

class ProductParameterValueCreate(BaseModel):
    product_id: int
    parameter_id: int
    value: str

class ProductParameterValueResponse(ProductParameterValueCreate):
    parameter_id: int
    value: str

    class Config:
        from_attributes = True

class DeliveryMethodCreate(BaseModel):
    method_name: str
    description: Optional[str] = None
    estimated_delivery_days: Optional[int] = None
    cost: float = Field(..., gt=0.0)

class DeliveryMethodResponse(DeliveryMethodCreate):
    id: int

    class Config:
        from_attributes = True

class PaymentMethodCreate(BaseModel):
    method_name: str
    description: Optional[str] = None
    fee: float = 0.00

class PaymentMethodResponse(PaymentMethodCreate):
    id: int

    class Config:
        from_attributes = True

class AddressCreate(BaseModel):
    address_line: str
    postal_code: str
    city: str
    country: str

class AddressBase(BaseModel):
    address_line: str
    postal_code: str
    city: str
    country: str

class AddressResponse(BaseModel):
    id: int
    address_line: str
    postal_code: str
    city: str
    country: str

    class Config:
        from_attributes=True

class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    role: Optional[str] = 'user'
    note: Optional[str] = None

    @validator('phone')
    def validate_phone(cls, v):
        if v and len(v) > 20:
            raise ValueError('Numer telefonu może mieć maksymalnie 20 znaków.')
        return v

    @validator('role')
    def validate_role(cls, v):
        if v and len(v) > 20:
            raise ValueError('Rola może mieć maksymalnie 20 znaków.')
        return v

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: Optional[str] = None
    note: Optional[str] = None

    @validator('phone')
    def validate_phone(cls, v):
        if v and len(v) > 20:
            raise ValueError('Numer telefonu może mieć maksymalnie 20 znaków.')
        return v

    @validator('role')
    def validate_role(cls, v):
        if v and len(v) > 20:
            raise ValueError('Rola może mieć maksymalnie 20 znaków.')
        return v

class UserResponse(UserBase):
    id: int
    address_id: Optional[int]
    created_at: str

    @validator('created_at', pre=True, always=True)
    def format_created_at(cls, v):
        if isinstance(v, datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        return v

    class Config:
        from_attributes = True

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    order_date: str
    delivery_method_id: Optional[int]
    payment_method_id: Optional[int]
    address_id: Optional[int]
    total_amount: float
    order_status: str
    order_items: List[OrderItemResponse]
    address: Optional[AddressResponse]
    
    class Config:
        from_attributes = True

    @validator('order_date', pre=True, always=True)
    def format_order_date(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return v

class OrderCreate(BaseModel):
    user_id: int
    delivery_method_id: Optional[int] = None
    payment_method_id: Optional[int] = None
    address: AddressCreate
    order_items: List[OrderItemCreate]
    total_amount: float

class UpdateOrderStatus(BaseModel):
    status: str

class PasswordResetRequest(BaseModel):
    email: str

class PasswordResetResponse(BaseModel):
    message: str

class PasswordResetValidationRequest(BaseModel):
    email: str
    token: str

class PasswordResetValidationResponse(BaseModel):
    message: str

class ChangePasswordRequest(BaseModel):
    email: str
    password: str

class OAuth2EmailPasswordRequestForm:
    def __init__(self, email: str = Form(), password: str = Form()):
        self.email = email
        self.password = password

class SubpageCreate(BaseModel):
    title: str
    path: str
    content: str
    is_active: bool

class SubpageUpdate(BaseModel):
    title: str | None = None
    path: str | None = None
    content: str | None = None
    is_active: bool | None = None

class TransactionRequest(BaseModel):
    amount: float
    description: str
    payer_email: str
    payer_name: str
    success_url: Optional[str] = None

class TransactionResponse(BaseModel):
    transaction_url: str

class ProductListItemCreate(BaseModel):
    user_id: int
    product_id: int

class UserId(BaseModel):
    user_id: int

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def encode_to_base64(data: Optional[bytes]) -> Optional[str]:
    if data is not None:
        return base64.b64encode(data).decode('utf-8')
    return None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=2)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def generate_token():
    characters = string.ascii_uppercase + string.digits  # A-Z, 0-9
    token = ''.join(random.choice(characters) for _ in range(6))
    return token

def send_email(email, token):
    recipient_email = email
    subject = "Reset hasła"
    body_html = """\
        <html>
        <body>
            <h3>
                Witaj!
            </h3>
            <p>
                Kod weryfikacyjny do zmiany hasła to: """ + token + """
            </p>
        </body>
        </html>
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html"))

    try:
        server = smtplib.SMTP(
            EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT
        )
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, recipient_email, msg.as_string())
        server.quit()

    except Exception as error:
        print(error)

async def get_db():
    async with SessionLocal() as session:
        yield session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Length", "Content-Type", "Authorization"],
)

@app.post("/register")
async def register(user: UserRegisterCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE email = :email"), {"email": user.email})
    existing_user = query.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Konto o podanym adresie e-mail już istnieje.")

    hashed_password = get_password_hash(user.password)
    db_user = User(first_name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return {"name": db_user.first_name, "email": db_user.email, "role": db_user.role, "id": user.id} 

@app.post("/login")
async def login(form_data: OAuth2EmailPasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE email = :email"), {"email": form_data.email})
    user = query.fetchone()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Nieprawidłowy adres e-mail lub hasło.")

    access_token = create_access_token(data={"name": user.first_name, "role": user.role, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer", "role": user.role, "id": user.id}

@app.post("/change-password")
async def change_password(request_data: ChangePasswordRequest, db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE email = :email"), {"email": request_data.email})
    user = query.fetchone()

    if not user:
        raise HTTPException(status_code=400, detail="Nieprawidłowy adres e-mail.")

    new_hashed_password = get_password_hash(request_data.password)
    await db.execute(text("UPDATE users SET hashed_password = :new_hashed_password WHERE email = :email"), 
                     {"new_hashed_password": new_hashed_password, "email": request_data.email})
    await db.commit()

    return {"message": "Hasło zostało zmienione."}

@app.post("/password-reset", response_model=PasswordResetResponse)
async def password_reset(request_data: PasswordResetRequest, db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT id, email FROM users WHERE email = :email"), {"email": request_data.email})
    user = query.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik o takim adresie e-mail nie istnieje.")

    password_reset_token = generate_token()
    token_expiration = datetime.utcnow() + timedelta(hours=1)

    await db.execute(
        text("""
            INSERT INTO password_reset_tokens (user_id, reset_token, token_expiration)
            VALUES (:user_id, :reset_token, :token_expiration)
        """),
        {"user_id": user.id, "reset_token": password_reset_token, "token_expiration": token_expiration}
    )
    await db.commit()

    send_email(email=user.email, token=password_reset_token)

    return {"message": "E-mail do zmiany hasła został wysłany."}

@app.post("/validate-password-reset", response_model=PasswordResetValidationResponse)
async def validate_password_reset(request_data: PasswordResetValidationRequest, db: AsyncSession = Depends(get_db)):
    query = await db.execute(
        text("""
            SELECT reset_token, token_expiration 
            FROM password_reset_tokens 
            JOIN users ON users.id = password_reset_tokens.user_id 
            WHERE users.email = :email
        """),
        {"email": request_data.email}
    )
    token_data = query.fetchone()

    if not token_data:
        raise HTTPException(status_code=400, detail="Użytkownik o takim adresie e-mail nie istnieje.")

    if token_data.reset_token != request_data.token:
        raise HTTPException(status_code=400, detail="Nieprawidłowy kod weryfikacyjny.")

    if token_data.token_expiration < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Kod weryfikacyjny wygasł.")

    return {"message": "Prawidłowo zweryfikowano kod."}

@app.post("/categories/")
async def create_category(category: ProductCategoryCreate, db: AsyncSession = Depends(get_db)):
    existing_category = await db.execute(
        select(ProductCategory).where(ProductCategory.category_name == category.category_name)
    )
    if existing_category.scalars().first() is not None:
        raise HTTPException(status_code=400, detail="Kategoria już istnieje.")

    db_category = ProductCategory(**category.dict())
    db.add(db_category)
    
    try:
        await db.commit()
        await db.refresh(db_category)
        return {"message": "Pomyślnie dodano kategorię."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/categories/", response_model=List[ProductCategoryResponse])
async def get_categories(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductCategory).offset(skip).limit(limit))
    categories = result.scalars().all()
    return categories

@app.get("/categories/{category_id}", response_model=ProductCategoryResponse)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductCategory).where(ProductCategory.id == category_id))
    category = result.scalars().first()

    if category is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono kategorii.")
    return category

@app.put("/categories/{category_id}")
async def update_category(category_id: int, category: ProductCategoryCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductCategory).where(ProductCategory.id == category_id))
    db_category = result.scalars().first()
    
    if db_category is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono kategorii.")

    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_category, key, value)

    await db.commit()
    await db.refresh(db_category)
    return {"message": "Pomyślnie zaktualizowano kategorię."}

@app.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductCategory).where(ProductCategory.id == category_id))
    db_category = result.scalars().first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono kategorii.")

    await db.delete(db_category)
    await db.commit()
    return {"message": "Pomyślnie usunięto kategorię."}

@app.post("/products/")
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    main_image = base64.b64decode(product.main_image) if product.main_image else None
    additional_images = [base64.b64decode(img) for img in product.additional_images] if product.additional_images else None

    db_product = Product(
        product_name=product.product_name,
        category_id=product.category_id,
        price=product.price,
        stock_quantity=product.stock_quantity,
        description=product.description,
        main_image=main_image,
        additional_images=additional_images
    )
    db.add(db_product)
    
    try:
        await db.commit()
        await db.refresh(db_product)

        response_product = {
            "id": db_product.id,
            "product_name": db_product.product_name,
            "category_id": db_product.category_id,
            "price": db_product.price,
            "stock_quantity": db_product.stock_quantity,
            "description": db_product.description,
            "main_image": base64.b64encode(db_product.main_image).decode('utf-8') if db_product.main_image else None,
            "additional_images": [
                base64.b64encode(img).decode('utf-8') for img in db_product.additional_images or []
            ],
            "created_at": db_product.created_at
        }
        
        return {"message": "Pomyślnie dodano produkt.", "product": response_product}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products/", response_model=List[ProductResponse])
async def get_products(
    skip: int = 0, 
    limit: int = 10,
    name: Optional[str] = Query(None), 
    id: Optional[int] = Query(None), 
    db: AsyncSession = Depends(get_db)
):
    if name is not None:
        query = select(Product).where(Product.product_name.ilike(f"%{name}%")).offset(skip).limit(limit)
    elif id is not None:
        query = select(Product).where(Product.id == id)
    else:
        query = select(Product).offset(skip).limit(limit)

    result = await db.execute(query)
    products = result.scalars().all()
    
    if products is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")
    return [ProductResponse.from_orm(product) for product in products]

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")
    return product

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: ProductCreate, db: AsyncSession = Depends(get_db)):
    main_image = base64.b64decode(product.main_image) if product.main_image else None
    additional_images = [base64.b64decode(img) for img in product.additional_images] if product.additional_images else None

    result = await db.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalar_one_or_none()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")
    
    db_product.product_name = product.product_name
    db_product.category_id = product.category_id
    db_product.price = product.price
    db_product.stock_quantity = product.stock_quantity
    db_product.description = product.description
    db_product.main_image = main_image
    db_product.additional_images = additional_images

    try:
        await db.commit()
        await db.refresh(db_product)
        return {"message": "Pomyślnie zaktualizowano produkt."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalar_one_or_none()
    
    if db_product is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")

    await db.delete(db_product)
    await db.commit()
    return {"message": "Pomyślnie usunięto produkt."}

@app.post("/parameters/", response_model=dict)
async def add_parameter(parameter: ProductParameterCreate, db: AsyncSession = Depends(get_db)):
    existing_parameter = await db.execute(select(ProductParameter).where(ProductParameter.parameter_name == parameter.parameter_name))
    if existing_parameter.scalars().first() is not None:
        raise HTTPException(status_code=400, detail="Parametr już istnieje.")

    db_parameter = ProductParameter(**parameter.dict())
    db.add(db_parameter)
    
    try:
        await db.commit()
        return {"message": "Pomyślnie dodano parametr."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/parameters/{parameter_id}")
async def delete_parameter(parameter_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductParameter).where(ProductParameter.id == parameter_id))
    db_parameter = result.scalar_one_or_none()
    if db_parameter is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru.")

    try:
        await db.delete(db_parameter)
        return {"message": "Pomyślnie usunięto parametr."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/parameters/{parameter_id}", response_model=dict)
async def edit_parameter(parameter_id: int, parameter: ProductParameterCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductParameter).where(ProductParameter.id == parameter_id))
    db_parameter = result.scalar_one_or_none()

    if db_parameter is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru.")
    
    existing_parameter = await db.execute(select(ProductParameter).where(ProductParameter.parameter_name == parameter.parameter_name))
    if existing_parameter.scalars().first() is not None:
        raise HTTPException(status_code=400, detail="Parameter już istnieje")

    db_parameter.parameter_name = parameter.parameter_name
    await db.commit()
    return {"message": "Pomyślnie zaktualizowano parametr."}

@app.get("/parameters/", response_model=List[ProductParameterResponse])
async def get_all_parameters(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductParameter))
    parameters = result.scalars().all()
    return parameters

@app.get("/parameters/{parameter_id}", response_model=ProductParameterResponse)
async def get_parameter(parameter_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductParameter).where(ProductParameter.id == parameter_id))
    parameter = result.scalar_one_or_none()
    if parameter is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru.")
    return parameter

@app.post("/product-parameters/", response_model=dict)
async def add_product_parameter_value(value: ProductParameterValueCreate, db: AsyncSession = Depends(get_db)):
    product_result = await db.execute(select(Product).where(Product.id == value.product_id))
    product = product_result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")

    parameter_result = await db.execute(select(ProductParameter).where(ProductParameter.id == value.parameter_id))
    parameter = parameter_result.scalar_one_or_none()
    if parameter is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru.")

    parameter_value_result = await db.execute(
        select(ParameterValue).where(
            ParameterValue.parameter_id == value.parameter_id,
            ParameterValue.value == value.value
        )
    )
    parameter_value = parameter_value_result.scalar_one_or_none()

    if parameter_value is None:
        new_parameter_value = ParameterValue(parameter_id=value.parameter_id, value=value.value)
        db.add(new_parameter_value)
        await db.commit()
        await db.refresh(new_parameter_value)

        db_product_parameter_value = ProductParameterValue(
            product_id=value.product_id,
            parameter_value_id=new_parameter_value.id
        )
        db.add(db_product_parameter_value)

    else:
        db_product_parameter_value = ProductParameterValue(
            product_id=value.product_id,
            parameter_value_id=parameter_value.id
        )
        db.add(db_product_parameter_value)

    try:
        await db.commit()
        return {"message": "Pomyślnie dodano parametr produktu."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/product-parameters/{product_id}", response_model=dict)
async def edit_product_parameter_value(product_id: int, value: ParameterValueCreate, db: AsyncSession = Depends(get_db)):
    product_result = await db.execute(select(Product).where(Product.id == product_id))
    product = product_result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu.")

    parameter_result = await db.execute(select(ProductParameter).where(ProductParameter.id == value.parameter_id))
    parameter = parameter_result.scalar_one_or_none()
    if parameter is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru.")

    existing_result = await db.execute(
        select(ProductParameterValue)
        .where(ProductParameterValue.product_id == product_id, 
               ProductParameterValue.parameter_value_id == value.parameter_id)
    )
    existing_parameter_value = existing_result.scalar_one_or_none()

    if existing_parameter_value is None:
        new_parameter_value = ProductParameterValue(
            product_id=value.product_id,
            parameter_value_id=value.parameter_id
        )
        db.add(new_parameter_value)
    else:
        existing_parameter_value.parameter_value_id = value.parameter_id
        existing_parameter_value.value = value.value

    try:
        await db.commit()
        return {"message": "Pomyślnie zaktualizowano parametr produktu."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/product-parameters/{product_parameter_value_id}")
async def delete_product_parameter_value(product_parameter_value_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProductParameterValue).where(ProductParameterValue.id == product_parameter_value_id))
    db_product_parameter_value = result.scalar_one_or_none()
    if db_product_parameter_value is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametru produktu.")

    await db.delete(db_product_parameter_value)
    try:
        await db.commit()
        return {"message": "Pomyślnie usunięto parametr produktu."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/product-parameters/{product_id}", response_model=list[ProductParameterValueResponse])
async def get_product_parameter_value(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(ProductParameterValue)
        .options(joinedload(ProductParameterValue.parameter_value))
        .where(ProductParameterValue.product_id == product_id)
    )
    product_parameter_values = result.scalars().all()

    if not product_parameter_values:
        raise HTTPException(status_code=404, detail="Nie znaleziono parametrów produktu.")

    response = [
        ProductParameterValueResponse(
            product_id=ppv.product_id,
            parameter_id=ppv.parameter_value.parameter_id,
            value=ppv.parameter_value.value
        )
        for ppv in product_parameter_values
    ]
    return response

@app.post("/delivery-methods/", response_model=DeliveryMethodResponse)
async def create_delivery_method(method: DeliveryMethodCreate, db: AsyncSession = Depends(get_db)):
    db_method = DeliveryMethod(**method.dict())
    db.add(db_method)
    await db.commit()
    await db.refresh(db_method)
    return db_method

@app.get("/delivery-methods/", response_model=list[DeliveryMethodResponse])
async def read_delivery_methods(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeliveryMethod))
    methods = result.scalars().all()
    return methods

@app.get("/delivery-methods/{method_id}", response_model=DeliveryMethodResponse)
async def read_delivery_method(method_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeliveryMethod).where(DeliveryMethod.id == method_id))
    method = result.scalar_one_or_none()
    if method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody dostawy.")
    return method

@app.put("/delivery-methods/{method_id}", response_model=DeliveryMethodResponse)
async def update_delivery_method(method_id: int, method: DeliveryMethodCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeliveryMethod).where(DeliveryMethod.id == method_id))
    db_method = result.scalar_one_or_none()
    if db_method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody dostawy.")
    
    db_method.method_name = method.method_name
    db_method.description = method.description
    db_method.estimated_delivery_days = method.estimated_delivery_days
    db_method.cost = method.cost
    
    await db.commit()
    await db.refresh(db_method)
    return db_method

@app.delete("/delivery-methods/{method_id}", response_model=dict)
async def delete_delivery_method(method_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeliveryMethod).where(DeliveryMethod.id == method_id))
    db_method = result.scalar_one_or_none()
    if db_method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody dostawy.")
    
    await db.delete(db_method)
    await db.commit()
    return {"message": "Pomyślnie usunięto metodę dostawy."}

@app.post("/payment-methods/", response_model=PaymentMethodResponse)
async def create_payment_method(method: PaymentMethodCreate, db: AsyncSession = Depends(get_db)):
    db_method = PaymentMethod(**method.dict())
    db.add(db_method)
    await db.commit()
    await db.refresh(db_method)
    return db_method

@app.get("/payment-methods/", response_model=List[PaymentMethodResponse])
async def read_payment_methods(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PaymentMethod))
    methods = result.scalars().all()
    return methods

@app.get("/payment-methods/{method_id}", response_model=PaymentMethodResponse)
async def read_payment_method(method_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PaymentMethod).where(PaymentMethod.id == method_id))
    method = result.scalar_one_or_none()
    if method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody płatności.")
    return method

@app.put("/payment-methods/{method_id}", response_model=PaymentMethodResponse)
async def update_payment_method(method_id: int, method: PaymentMethodCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PaymentMethod).where(PaymentMethod.id == method_id))
    db_method = result.scalar_one_or_none()
    if db_method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody płatności.")
    
    db_method.method_name = method.method_name
    db_method.description = method.description
    db_method.fee = method.fee
    
    await db.commit()
    await db.refresh(db_method)
    return db_method

@app.delete("/payment-methods/{method_id}", response_model=dict)
async def delete_payment_method(method_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PaymentMethod).where(PaymentMethod.id == method_id))
    db_method = result.scalar_one_or_none()
    if db_method is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono metody płatności.")
    
    await db.delete(db_method)
    await db.commit()
    return {"message": "Pomyślnie usunięto metodę płatności."}

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await db.execute(select(User).where(User.email == user.email))
    if existing_user.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Użytkownik o podanym adresie e-mail jest już zarejestrowany.")

    new_user = User(**user.dict())
    new_user.hashed_password =  get_password_hash(user.hashed_password)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    
    return [UserResponse.from_orm(user) for user in users]

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono użytkownika.")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono użytkownika.")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)
    return user

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono użytkownika.")

    await db.delete(user)
    await db.commit()
    return {"message": "Pomyślnie usunięto użytkownika."}

@app.post("/addresses/", response_model=AddressResponse)
async def create_address(
    address: AddressCreate, user_id: Optional[int] = None, db: AsyncSession = Depends(get_db)
):
    db_address = Address(
        address_line=address.address_line,
        postal_code=address.postal_code,
        city=address.city,
        country=address.country
    )
    
    db.add(db_address)
    await db.commit()
    await db.refresh(db_address)

    if user_id:
        result = await db.execute(select(User).where(User.id == user_id).options(selectinload(User.address)))
        user = result.scalar_one_or_none()

        if user:
            user.address_id = db_address.id
            await db.commit()
            await db.refresh(user)
        else:
            raise HTTPException(status_code=404, detail="Nie znaleziono użytkownika.")

    return db_address

@app.get("/addresses/{address_id}", response_model=AddressResponse)
async def get_address(address_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Address).filter(Address.id == address_id))
    address = result.scalar_one_or_none()
    if not address:
        raise HTTPException(status_code=404, detail="Nie znaleziono adresu.")
    return AddressResponse.from_orm(address)

@app.put("/addresses/{address_id}", response_model=AddressResponse)
async def update_address(address_id: int, address: AddressCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Address).filter(Address.id == address_id))
    db_address = result.scalar_one_or_none()
    if not db_address:
        raise HTTPException(status_code=404, detail="Nie znaleziono adresu.")

    db_address.address_line = address.address_line
    db_address.postal_code = address.postal_code
    db_address.city = address.city
    db_address.country = address.country

    await db.commit()
    await db.refresh(db_address)
    return AddressResponse.from_orm(db_address)

@app.delete("/addresses/{address_id}", response_model=dict)
async def delete_address(address_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Address).filter(Address.id == address_id))
    db_address = result.scalar_one_or_none()
    if not db_address:
        raise HTTPException(status_code=404, detail="Nie znaleziono adresu.")

    await db.delete(db_address)
    await db.commit()
    return {"message": "Pomyślnie usunięto adres."}

@app.post("/orders/", response_model=dict)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    if order.address:
        db_address = Address(**order.address.dict())
        db.add(db_address)
        await db.commit()
        await db.refresh(db_address)
        address_id = db_address.id
    else:
        address_id = None

    db_order = Order(
        user_id=order.user_id,
        delivery_method_id=order.delivery_method_id,
        payment_method_id=order.payment_method_id,
        address_id=address_id,
        total_amount=order.total_amount
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    for item in order.order_items:
        existing_item_result = await db.execute(
            select(OrderItem).where(
                OrderItem.order_id == db_order.id,
                OrderItem.product_id == item.product_id
            )
        )
        existing_item = existing_item_result.scalar_one_or_none()

        if existing_item:
            existing_item.quantity += item.quantity
            existing_item.price = item.price
        else:
            db_order_item = OrderItem(
                order_id=db_order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            db.add(db_order_item)

    try:
        await db.commit()
        return {"message": "Pomyślnie dodano zamówienie."}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="W zamówieniu podano zduplikowane produkty.")
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/orders/", response_model=List[OrderResponse])
async def get_orders(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(
            select(Order)
            .options(joinedload(Order.order_items), joinedload(Order.address))
        )
        
        orders = result.unique().scalars().all()

        return [
            {
                "id": order.id,
                "user_id": order.user_id,
                "order_date": order.order_date.isoformat(),
                "delivery_method_id": order.delivery_method_id,
                "payment_method_id": order.payment_method_id,
                "address_id": order.address_id,
                "total_amount": order.total_amount,
                "order_status": order.order_status,
                "order_items": [
                    {
                        "id": item.id,
                        "product_id": item.product_id,
                        "quantity": item.quantity,
                        "price": item.price,
                    } for item in order.order_items
                ],
                "address": AddressResponse.from_orm(order.address) if order.address else None
            }
            for order in orders
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order)
        .options(selectinload(Order.order_items), selectinload(Order.address))
        .where(Order.id == order_id)
    )

    order = result.scalars().unique().one_or_none()
    
    if order is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono zamówienia.")
    
    return OrderResponse(
        id=order.id,
        user_id=order.user_id,
        order_date=order.order_date.isoformat(),
        delivery_method_id=order.delivery_method_id,
        payment_method_id=order.payment_method_id,
        address_id=order.address_id,
        total_amount=order.total_amount,
        order_status=order.order_status,
        order_items=[
            {
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price,
            } for item in order.order_items
        ],
        address=AddressResponse.from_orm(order.address) if order.address else None
    )

@app.put("/orders/{order_id}/status", response_model=dict)
async def update_order_status(order_id: int, update_status: UpdateOrderStatus, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    db_order = result.scalar_one_or_none()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono zamówienia.")

    db_order.order_status = update_status.status
    await db.commit()
    return {"message": "Pomyślnie zaktualizowano zamówienie."}

@app.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    db_order = result.scalar_one_or_none()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono zamówienia.")
    
    await db.delete(db_order)
    await db.commit()
    return {"message": "Pomyślnie usunięto zamówienie."}

@app.post("/subpages/")
async def create_subpage(subpage: SubpageCreate, db: AsyncSession = Depends(get_db)):
    await db.execute(
        text("""
            INSERT INTO subpages (title, path, content, is_active) 
            VALUES (:title, :path, :content, :is_active)
        """),
        {
            "title": subpage.title,
            "path": subpage.path,
            "content": subpage.content,
            "is_active": subpage.is_active
        }
    )
    await db.commit()
    return {"message": "Pomyślnie dodano podstronę."}

@app.put("/subpages/{subpage_id}")
async def update_subpage(subpage_id: int, subpage: SubpageUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM subpages WHERE id = :id"), {"id": subpage_id})
    db_subpage = result.fetchone()
    if db_subpage is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono podstrony.")

    update_fields = {key: value for key, value in subpage.dict(exclude_unset=True).items()}

    if update_fields:
        set_clause = ", ".join(f"{key} = :{key}" for key in update_fields.keys())
        update_fields["id"] = subpage_id
        await db.execute(text(f"UPDATE subpages SET {set_clause} WHERE id = :id"), update_fields)
        await db.commit()

    return {"message": "Pomyślnie zaktualizowano podstronę."}

@app.delete("/subpages/{subpage_id}")
async def delete_subpage(subpage_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM subpages WHERE id = :id"), {"id": subpage_id})
    db_subpage = result.fetchone()
    if db_subpage is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono podstrony.")

    await db.execute(text("DELETE FROM subpages WHERE id = :id"), {"id": subpage_id})
    await db.commit()
    return {"message": "Pomyślnie usunięto podstronę."}

@app.get("/subpages/")
async def get_subpages(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM subpages"))
    subpages = result.mappings().all()
    return subpages

@app.get("/subpages/{subpage_id}")
async def get_subpage(subpage_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM subpages WHERE id = :id"), {"id": subpage_id})
    subpage = result.mappings().first()
    if subpage is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono podstrony.")
    return subpage

async def get_tpay_token():
    """Generate a TPay access token."""
    async with AsyncClient() as client:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }
        response = await client.post(TPAY_AUTH_URL, headers=headers, data=data)
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch access token.")
        
        token_data = response.json()
        return token_data.get("access_token")


@app.post("/transactions", response_model=TransactionResponse)
async def create_transaction(request: TransactionRequest):
    """
    Create a TPay transaction and return the transaction URL.
    """
    access_token = await get_tpay_token()
    print(request.success_url)

    if not access_token:
        raise HTTPException(status_code=500, detail="Access token generation failed.")
    
    async with AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "amount": request.amount,
            "description": request.description,
            "payer": {
                "email": request.payer_email,
                "name": request.payer_name,
            },
            "callbacks": {
                "payerUrls": {
                    "success": request.success_url if request.success_url else "https://tpay.com",
                },
            }
        }
        response = await client.post(TPAY_TRANSACTION_URL, headers=headers, json=payload)
        response = response.json()
        
        if response.get("result") != "success":
            raise HTTPException(
                status_code=response.get("result"),
                detail=f"Failed to create transaction: {response}"
            )
        
        transaction_url = response.get("transactionPaymentUrl")

        if not transaction_url:
            raise HTTPException(status_code=500, detail="Transaction URL not provided by TPay.")
        
        return TransactionResponse(transaction_url=transaction_url)
    
async def get_or_create_user_list(user_id: int, db: AsyncSession):
    result = await db.execute(
        text("SELECT id FROM product_lists WHERE user_id = :user_id AND list_name = 'Favorites'"),
        {"user_id": user_id}
    )
    user_list = result.fetchone()
    
    if not user_list:
        result = await db.execute(
            text("""
                INSERT INTO product_lists (user_id, list_name, description) 
                VALUES (:user_id, 'Favorites', 'User favorites list') RETURNING id
            """),
            {"user_id": user_id}
        )
        user_list = result.fetchone()
        await db.commit()

    return user_list[0]

@app.post("/favorites/")
async def add_product_to_favorites(item: ProductListItemCreate, db: AsyncSession = Depends(get_db)):
    product_list_id = await get_or_create_user_list(item.user_id, db)

    try:
        await db.execute(
            text("""
                INSERT INTO product_list_items (product_list_id, product_id) 
                VALUES (:product_list_id, :product_id)
            """),
            {"product_list_id": product_list_id, "product_id": item.product_id}
        )
        await db.commit()
        return {"message": "Pomyślnie dodano produkt do listy ulubionych."}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Produkt już znajduje się w liście ulubionych.")

@app.delete("/favorites/{product_id}")
async def remove_product_from_favorites(product_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    product_list_id = await get_or_create_user_list(user_id, db)

    result = await db.execute(
        text("DELETE FROM product_list_items WHERE product_list_id = :product_list_id AND product_id = :product_id"),
        {"product_list_id": product_list_id, "product_id": product_id}
    )

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Nie znaleziono produktu w liście ulubionych..")

    await db.commit()
    return {"message": "Pomyślnie usunięto produkt do listy ulubionych."}

@app.get("/favorites/{user_id}")
async def get_favorite_products(user_id: int, db: AsyncSession = Depends(get_db)):
    product_list_id = await get_or_create_user_list(user_id, db)

    result = await db.execute(
        text("""
            SELECT p.id, p.product_name, p.price, p.description 
            FROM products p
            JOIN product_list_items pli ON pli.product_id = p.id
            WHERE pli.product_list_id = :product_list_id
        """),
        {"product_list_id": product_list_id}
    )

    products = result.mappings().all()
    return products