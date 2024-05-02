from config import config
from connect import HHParser
from database import create_database
from tables import creating_tables
from tables import data_entry
from dbmanager import DBManager
def main():
    list_id = [1479944, 64174, 3530, 8550, 13819, 48735, 50233, 51296, 55125, 56433]
    #dbname = 'courswork5'
    #hh = HHParser(list_id)
    ##print(hh.job_employers())
    #print(hh.get_employers_list())
    #print(hh.filter_salary())
    params = config()
    # create_database(params)
    # creating_tables(params)
    # data_entry(params, list_id)
    dbm = DBManager()
    print(dbm.get_companies_and_vacancies_count(params))


if __name__ == '__main__':
    main()