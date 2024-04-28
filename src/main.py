from config import config
from connect import HHParser
from database import create_database
from tables import creating_tables
from tables import data_entry
def main():
    params = config()
    hh = HHParser()
    create_database(params)
    creating_tables(params)
    data_entry(params)


if __name__ == '__main__':
    main()