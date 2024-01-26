import file_helper
import logging
import os

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)


global MAIN_DIRECTORY
MAIN_DIRECTORY = os.path.dirname(__file__)

if __name__ == '__main__':
    file_config = file_helper.read_config_file(config_type="metadata")
    print(file_config)
    print(type(file_config))
    print(file_config["file_location"])
    db_config = file_helper.read_config_file(config_type="database")
    print(db_config)
    logging.info("We are here")

    for key,value in file_config.items():
        logging.info(f"{key}: {value}")