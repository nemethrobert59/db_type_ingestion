import psycopg2
import yaml
import os
import pandas as pd
from sqlalchemy import create_engine, text
import file_helper

MAIN_DIRECTORY = os.path.dirname(__file__)

def establish_connection():
    with open(r'C:\Users\nemet\OneDrive\Dokumentumok\GitHub\db_type_ingestion\postgres_config.yaml', 'r') as file:
        config = yaml.safe_load(file)['postgres']

    connection = psycopg2.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        dbname='postgres'  # Connect to the default database to create a new one
    )
    connection.autocommit = True

    return connection, config

def create_database(connection,config):
    with connection.cursor() as cursor:
        try:
            #cursor.execute(f"DROP DATABASE {config['db_name']};")
            cursor.execute(f"CREATE DATABASE {config['db_name']};")
            print(f"Database {config['db_name']} created successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()

def get_database_version(connection,config):
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()[0]
            print(f"Your {config['db_name']} database version is the following: {db_version}")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            cursor.close()

def create_my_table_statement(connection, ddl_statement):
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"{ddl_statement}")
            print(f"Your table has been created.")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            cursor.close()

def create_database_engine(config):
    engine = create_engine(f'postgresql://{config["user"]}:{config["password"]}@{config["host"]}/{config["db_name"]}')
    print(engine)
    return engine

def load_data_from_file(engine,df,table_name):
    df.to_sql(schema = "public",name = table_name, con = engine, if_exists="replace", index=False)

def get_record_count(table_name,schema_name = "public"):
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {schema_name}.{table_name};")
            print(cursor.fetchone()[0])
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            cursor.close()



if __name__ == '__main__':
    connection, config = establish_connection()
    create_database(connection, config)
    get_database_version(connection, config)
    ddl_statement = file_helper.open_ddl_statement(main_directory=MAIN_DIRECTORY)
    create_my_table_statement(connection, ddl_statement)
    engine = create_database_engine(config)
    df = file_helper.read_input_file(main_directory=MAIN_DIRECTORY,file_name="test_data.csv")
    print(df)
    connection.close()
    with engine.begin() as conn:
        df.to_sql(schema="public", name="customer_data", con=conn, if_exists="replace", index=False)
    with engine.connect() as conn:
        conn.execute(text("SELECT * FROM public.customer_data;")).fetchall()
    #get_record_count(table_name="customer_data")
