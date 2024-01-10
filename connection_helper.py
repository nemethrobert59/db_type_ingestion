import psycopg2
import yaml

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

def create_my_table_statement(connection):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""CREATE TABLE market_data (
                            id SERIAL PRIMARY KEY,
                            datetime TIMESTAMP NOT NULL,
                            open NUMERIC(10, 2),
                            high NUMERIC(10, 2),
                            low NUMERIC(10, 2),
                            close NUMERIC(10, 2),
                            volume BIGINT
                            );""")
            print(f"Your table has been created.")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            cursor.close()


if __name__ == '__main__':
    connection, config = establish_connection()
    create_database(connection, config)
    get_database_version(connection, config)
    create_my_table_statement(connection)
    connection.close()
