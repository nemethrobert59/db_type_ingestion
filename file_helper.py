import os

def open_my_file(main_directory):
    with open(os.path.join(main_directory,"ddl\market_data.sql"), 'r') as file:
        ddl_statement = file.read()
    return ddl_statement