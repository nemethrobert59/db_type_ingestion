import file_helper
import logging
import os

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

MAIN_DIRECTORY = os.path.dirname(__file__)

config_file_name = "fundamentals_config.yml"

if __name__ == '__main__':
    file_config = file_helper.read_config_file(config_file_name)
    print(file_config["metadata"])
    print(file_config["database"]["db_type"])


    #for key,value in file_config.items():
    #    print(f"{key}: {value}")