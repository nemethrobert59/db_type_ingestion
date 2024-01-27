from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_database_version(engine):
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            db_version = result.fetchone()[0]
            print(f"Your database version is the following: {db_version}")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")