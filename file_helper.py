import os
import pandas as pd
import yaml
from main import MAIN_DIRECTORY

def read_config_file(config_file_path):
    with open(os.path.join(MAIN_DIRECTORY,rf"{config_file_path}"), 'r') as file:
        config = yaml.safe_load(file)
    return config

def read_input_file(main_directory,file_name):
    file_path = os.path.join(main_directory,"data",file_name)
    print(file_path)
    df = pd.read_csv(file_path)
    return df