CREATE TABLE IF NOT EXISTS products (
                                        id SERIAL PRIMARY KEY,
                                        category VARCHAR(255),
    subcategory VARCHAR(255),
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2)
    );
