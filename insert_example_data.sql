INSERT INTO addresses (address_line, postal_code, city, country) VALUES
('ul. Krakowska 15', '31-060', 'Kraków', 'Polska'),
('ul. Mazowiecka 4', '00-048', 'Warszawa', 'Polska'),
('ul. Grunwaldzka 12/5', '80-244', 'Gdańsk', 'Polska'),
('ul. Piotrkowska 10', '90-001', 'Łódź', 'Polska'),
('ul. Świdnicka 8', '50-066', 'Wrocław', 'Polska');

INSERT INTO users (first_name, last_name, email, phone, hashed_password, address_id, role, note) VALUES
('Jan', 'Kowalski', 'jan.kowalski@example.com', '600100200', 'hashed_pass_123', 1, 'admin', 'Administrator systemu'),
('Anna', 'Nowak', 'anna.nowak@example.com', '600300400', 'hashed_pass_456', 2, 'user', NULL),
('Piotr', 'Zieliński', 'piotr.zielinski@example.com', '700200300', 'hashed_pass_789', 3, 'user', 'Stały klient'),
('Ewa', 'Wiśniewska', 'ewa.wisniewska@example.com', '800500600', 'hashed_pass_012', 4, 'user', NULL),
('Kamil', 'Jankowski', 'kamil.jankowski@example.com', '900400500', 'hashed_pass_345', 5, 'user', 'Preferuje kontakt mailowy');

INSERT INTO product_categories (category_name, parent_category_id, description) VALUES
('Elektronika', NULL, 'Sprzęt elektroniczny i akcesoria'),
('Komputery', 1, 'Komputery stacjonarne i laptopy'),
('Smartfony', 1, 'Telefony komórkowe i akcesoria'),
('AGD', NULL, 'Sprzęt AGD do domu'),
('Telewizory', 1, 'Telewizory i akcesoria');

INSERT INTO products (product_name, category_id, price, stock_quantity, description) VALUES
('Laptop Dell Inspiron 15', 1, 3499.99, 10, 'Laptop Dell z procesorem Intel i5, 8 GB RAM, SSD 512 GB'),
('Smartfon Samsung Galaxy S21', 2, 2999.00, 20, 'Smartfon z ekranem AMOLED 6.2 cala, 128 GB pamięci'),
('Telewizor LG OLED55', 3, 5999.00, 5, 'Telewizor OLED 55 cali 4K UHD z obsługą HDR'),
('Lodówka Samsung RB34T', 4, 2499.00, 8, 'Lodówka z technologią No Frost, klasa energetyczna A++'),
('Klawiatura mechaniczna Logitech G Pro', 5, 499.00, 15, 'Klawiatura mechaniczna dla graczy z podświetleniem RGB');
