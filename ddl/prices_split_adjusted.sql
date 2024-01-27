CREATE TABLE market_data.prices-split-adjusted (
    date DATE,
    symbol VARCHAR(10),
    open NUMERIC(10, 6),
    close NUMERIC(10, 6),
    low NUMERIC(10, 6),
    high NUMERIC(10, 6),
    volume NUMERIC
);