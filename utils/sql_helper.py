from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from sqlalchemy import INTEGER, VARCHAR, DATE, NUMERIC, BIGINT, TEXT, DOUBLE_PRECISION

def get_database_version(engine):
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            db_version = result.fetchone()[0]
            print(f"Your database version is the following: {db_version}")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

def sqlalchemy_to_pandas_mapping(column_definitions):
    # Mapping from SQLAlchemy to pandas/numpy data types
    type_mapping = {
        BIGINT: 'int64',
        TEXT: 'object',
        DOUBLE_PRECISION: 'float64',
        INTEGER: 'int64',
        VARCHAR: 'object',
        DATE: 'object',
        NUMERIC: 'float64'
    }

    # Creating the pandas dtype dictionary
    pandas_dtypes = {}
    for col_name, col_type in column_definitions:
        # Extracting the type class from the SQLAlchemy type instance
        type_class = type(col_type)
        pandas_dtype = type_mapping.get(type_class, 'object')  # Default to 'object' if type not found
        pandas_dtypes[col_name] = pandas_dtype

    return pandas_dtypes