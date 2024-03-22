from sqlalchemy import create_engine, text
import file_helper

def create_database_engine(db_type, username, password, host, port, db_name):
    if db_type == 'postgres':
        engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')
    else:
        print(f"The {db_type} has not been implemented yet.")
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
    with engine.begin() as conn:
        df.to_sql(schema="public", name="customer_data", con=conn, if_exists="replace", index=False)
        conn.execute(text("SELECT * FROM public.customer_data;")).fetchall()
    get_record_count(table_name="customer_data")
    connection.close()
