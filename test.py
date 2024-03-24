import logging
import os
from utils import connection_helper
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from utils import sql_helper

logging.basicConfig(format='##############################\n\
%(asctime)s - %(levelname)s: %(message)s\
\n##############################', datefmt='%Y-%m-%d %H:%M:%S %Z', level=logging.DEBUG)

MAIN_DIRECTORY = os.path.dirname(__file__)


if __name__ == '__main__':
    print("Start of the development")
    print(str(MAIN_DIRECTORY))    
