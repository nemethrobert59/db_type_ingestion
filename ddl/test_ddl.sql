CREATE TABLE customer_data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    registration_date DATE,
    is_active BOOLEAN,
    balance DECIMAL(10, 2),
    notes TEXT,
    last_login_time TIMESTAMP
);