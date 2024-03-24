from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

logger = logging.getLogger()

def create_database_engine(db_type, username, password, host, port, db_name):
    if db_type == 'postgres':
        engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')
    else:
        print(f"The {db_type} has not been implemented yet.")
    
    try:
        engine.connect()
        logger.info(f"You are connected to the {db_name} on the {host} host with the {username} user")
    except SQLAlchemyError as err:
        logger.error("error", err.__cause__)

    return engine

def load_data_from_file(engine,df,table_name):
    df.to_sql(schema = "public",name = table_name, con = engine, if_exists="replace", index=False)