import os

MAIN_DIRECTORY = os.path.dirname(__file__)
print(MAIN_DIRECTORY)

def open_my_file(main_directory):
    with open(os.path.join(main_directory,"\ddl\market_data.sql"), 'r') as file:
        print(file)


open_my_file(main_directory = MAIN_DIRECTORY)