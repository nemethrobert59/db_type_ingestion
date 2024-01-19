import os
import pandas as pd
import yaml

def open_ddl_statement(main_directory):
    with open(os.path.join(main_directory,"ddl\\test_ddl.sql"), 'r') as file:
        ddl_statement = file.read()
    return ddl_statement

def read_config_file(config_type):
    with open(r'C:\Users\nemet\OneDrive\Dokumentumok\GitHub\db_type_ingestion\metadata\data_load_config.yaml', 'r') as file:
        config = yaml.safe_load(file)[config_type]
    return config

def read_input_file(main_directory,file_name):
    file_path = os.path.join(main_directory,"data",file_name)
    print(file_path)
    df = pd.read_csv(file_path)
    return df