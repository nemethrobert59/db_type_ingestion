import file_helper
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

if __name__ == '__main__':
    file_config = file_helper.read_config_file(config_type="metadata")
    print(file_config)
    print(file_config["file_location"])
    db_config = file_helper.read_config_file(config_type="database")
    print(db_config)
    logging.info("We are here")