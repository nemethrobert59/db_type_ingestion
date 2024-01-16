import psycopg2
import yaml
import os
from sqlalchemy import create_engine, text
import pandas as pd
import random
from datetime import datetime, timedelta
import time


# Function to generate mock data
def generate_mock_data(num_rows):
    data = []
    for _ in range(num_rows):
        id = random.randint(1000, 9999)
        name = f"Name_{random.randint(1, 100)}"
        date = datetime.now() - timedelta(days=random.randint(1, 365))
        value = random.uniform(10, 1000)
        data.append([id, name, date, value])

    columns = ['id', 'name', 'date', 'value']
    df = pd.DataFrame(data, columns=columns)
    return df


def create_database_engine(config):
    engine = create_engine(f'postgresql://{config["user"]}:{config["password"]}@{config["host"]}/{config["db_name"]}')
    return engine



if __name__ == '__main__':
    with open(r'C:\Users\nemet\OneDrive\Dokumentumok\GitHub\db_type_ingestion\postgres_config.yaml', 'r') as file:
        config = yaml.safe_load(file)['postgres']

    engine = create_database_engine(config)

    start_time = time.time()  # get start time before insert

    df = generate_mock_data(num_rows=1000000)
    with engine.begin() as conn:
        #df.to_sql(schema="public", name="my_target_table", con=conn, if_exists="replace", index=False)
        #result = conn.execute(text("SELECT COUNT(*) FROM public.my_target_table;")).fetchone()
        #print(result[0])
        result = conn.exec_driver_sql(
            """\
            DELETE FROM my_target_table
            WHERE EXISTS (
                SELECT 1
                FROM my_target_table_all_pk
                WHERE my_target_table.id = my_target_table_all_pk.id
            );
            """
        )
        # Get the number of rows deleted
        deleted_rows_count = result.rowcount
        print(f"Number of records deleted: {deleted_rows_count}")
        result2 = conn.exec_driver_sql(
        """\
        INSERT INTO my_target_table (id, name, date, value) 
        SELECT id, name, date, value FROM my_target_table_all_record
        ON CONFLICT (id) DO
            UPDATE SET name = EXCLUDED.name, date = EXCLUDED.date, value = EXCLUDED.value
        """)
        updated_rows_count = result2.rowcount
        print(f"Number of records deleted: {updated_rows_count}")

    end_time = time.time()  # get end time after insert
    total_time = end_time - start_time  # calculate the time
    print(f"Insert time: {total_time} seconds")  # print time
