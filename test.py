from utils import connection_helper
from utils import sql_helper
import logging
import os
from sqlalchemy import create_engine, text, select
import pandas as pd
import argparse

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

logger = logging.getLogger()

MAIN_DIRECTORY = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description='Specify the metadata config system_name')
parser.add_argument('--system_name',help='Use the appropriate system_name from the metadata folder without file extension.')
args = parser.parse_args()
system_name = args.system_name

if __name__ == '__main__':
    logger.info("The Engagement Platform ETL has been started")

    engine = connection_helper.create_database_engine(db_type = 'postgres',
    username = 'admin',
    password = 'admin',
    host = 'metadata',
    port = '5432',
    db_name = 'metadata')

    df = pd.read_sql(f"select * from meta.ep_metadata where system_name = '{system_name}'", con=engine)

    for i in range(len(df)):
        logger.info("The following metadata will be processed:")
        meta_df = df.iloc[i]
        print(meta_df)

        csv_file_path = MAIN_DIRECTORY + "/data/fundamentals.csv"

        print(csv_file_path)
        
        with open(csv_file_path, 'r') as file:
            data_df = pd.read_csv(file)
        #data_df.to_sql('tbl_name', con=engine, index=True, index_label='id', if_exists='replace')

    
    #for index, row in df.iterrows():
    #    logger.info("The following metadata will be processed:")
    #    for column_name in df.columns:
    #        value = row[column_name]
    #        print(f"{column_name}: {value}")

