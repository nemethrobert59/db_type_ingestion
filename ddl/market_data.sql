CREATE TABLE my_schema.market_data (id SERIAL PRIMARY KEY,
datetime TIMESTAMP NOT NULL,
open NUMERIC(10, 2),
high NUMERIC(10, 2),
low NUMERIC(10, 2),
close NUMERIC(10, 2),
volume BIGINT
);