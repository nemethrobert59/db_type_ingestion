import file_helper
import logging
import os
import connection_helper
from sqlalchemy import inspect, INTEGER, VARCHAR, DATE, NUMERIC
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import sql_helper

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

MAIN_DIRECTORY = os.path.dirname(__file__)


if __name__ == '__main__':
    metadata_config = file_helper.read_config_file(config_file_path = "metadata/fundamentals_config.yml")
    table_name = metadata_config["metadata"]["table_name"]

    db_config = file_helper.read_config_file(config_file_path="docker_compose_postgres.yml")

    db_type = metadata_config["database"]["db_type"]
    db_name = db_config["services"]["db"]["environment"]["POSTGRES_DB"]
    username = db_config["services"]["db"]["environment"]["POSTGRES_USER"]
    password = db_config["services"]["db"]["environment"]["POSTGRES_PASSWORD"]
    host = "localhost"
    port = db_config["services"]["db"]["ports"][0].split(':')[0]

    engine = connection_helper.create_database_engine(db_type,
                                                      username,
                                                      password,
                                                      host,
                                                      port,
                                                      db_name)

    try:
        engine.connect()
        print(f"You are connected to the {db_name} on the {host} host with the {username}")
    except SQLAlchemyError as err:
        print("error", err.__cause__)

    sql_helper.get_database_version(engine)

    file_path = os.path.join(MAIN_DIRECTORY,"data",table_name + ".csv")

    with engine.begin() as connection:
        insp = inspect(engine)
        columns_table = insp.get_columns(table_name,schema="market_data")

        column_names = [col['name'] for col in columns_table]
        column_types = [col['type'] for col in columns_table]
        print(column_types)

        column_details = [(col['name'], col['type']) for col in columns_table]

        print(column_details)

        df = pd.read_csv(file_path,header=1, names=column_names,na_values="NaN")
        print(df)
        df.to_sql(table_name, connection,schema="market_data", if_exists='replace', index=False)
