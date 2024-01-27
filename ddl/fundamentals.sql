CREATE TABLE market_data.fundamentals (
    id SERIAL PRIMARY KEY,
    ticker_symbol VARCHAR(10),
    period_ending DATE,
    accounts_payable NUMERIC,
    accounts_receivable NUMERIC,
    additional_income_expense_items NUMERIC,
    after_tax_roe NUMERIC,
    capital_expenditures NUMERIC,
    capital_surplus NUMERIC,
    cash_ratio NUMERIC,
    cash_and_cash_equivalents NUMERIC,
    changes_in_inventories NUMERIC,
    common_stocks NUMERIC,
    cost_of_revenue NUMERIC,
    current_ratio NUMERIC,
    deferred_asset_charges NUMERIC,
    deferred_liability_charges NUMERIC,
    depreciation NUMERIC,
    earnings_before_interest_and_tax NUMERIC,
    earnings_before_tax NUMERIC,
    effect_of_exchange_rate NUMERIC,
    equity_earnings_loss_unconsolidated_subsidiary NUMERIC,
    fixed_assets NUMERIC,
    goodwill NUMERIC,
    gross_margin NUMERIC,
    gross_profit NUMERIC,
    income_tax NUMERIC,
    intangible_assets NUMERIC,
    interest_expense NUMERIC,
    inventory NUMERIC,
    investments NUMERIC,
    liabilities NUMERIC,
    long_term_debt NUMERIC,
    long_term_investments NUMERIC,
    minority_interest NUMERIC,
    misc_stocks NUMERIC,
    net_borrowings NUMERIC,
    net_cash_flow NUMERIC,
    net_cash_flow_operating NUMERIC,
    net_cash_flows_financing NUMERIC,
    net_cash_flows_investing NUMERIC,
    net_income NUMERIC,
    net_income_adjustments NUMERIC,
    net_income_applicable_to_common_shareholders NUMERIC,
    net_income_cont_operations NUMERIC,
    net_receivables NUMERIC,
    non_recurring_items NUMERIC,
    operating_income NUMERIC,
    operating_margin NUMERIC,
    other_assets NUMERIC,
    other_current_assets NUMERIC,
    other_current_liabilities NUMERIC,
    other_equity NUMERIC,
    other_financing_activities NUMERIC,
    other_investing_activities NUMERIC,
    other_liabilities NUMERIC,
    other_operating_activities NUMERIC,
    other_operating_items NUMERIC,
    pre_tax_margin NUMERIC,
    pre_tax_roe NUMERIC,
    profit_margin NUMERIC,
    quick_ratio NUMERIC,
    research_and_development NUMERIC,
    retained_earnings NUMERIC,
    sale_and_purchase_of_stock NUMERIC,
    sales_general_and_admin NUMERIC,
    short_term_debt_current_portion_of_long_term_debt NUMERIC,
    short_term_investments NUMERIC,
    total_assets NUMERIC,
    total_current_assets NUMERIC,
    total_current_liabilities NUMERIC,
    total_equity NUMERIC,
    total_liabilities NUMERIC,
    total_liabilities_and_equity NUMERIC,
    total_revenue NUMERIC,
    treasury_stock NUMERIC,
    for_year INT,
    earnings_per_share NUMERIC,
    estimated_shares_outstanding NUMERIC
);