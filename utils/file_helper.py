import os
import pandas as pd
from main import MAIN_DIRECTORY

def read_input_file(main_directory,file_name):
    file_path = os.path.join(main_directory,"data",file_name)
    print(file_path)
    df = pd.read_csv(file_path)
    return df