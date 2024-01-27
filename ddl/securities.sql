CREATE TABLE market_data.securities (
    ticker_symbol VARCHAR(10),
    security VARCHAR(100),
    sec_filings VARCHAR(50),
    gics_sector VARCHAR(50),
    gics_sub_industry VARCHAR(100),
    address_of_headquarters VARCHAR(255),
    date_first_added DATE,
    cik VARCHAR(10)
);