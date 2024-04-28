import psycopg2
#from config import config

def create_database(params):
    '''
    Создаем базу данных courswork5
    '''
    conn = psycopg2.connect(dbname='postgres',**params)
# conn = psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="qwerty",
#     port=5432
# )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS courswork5")
    cur.execute("CREATE DATABASE courswork5")

    cur.close()
    conn.close()


#create_database()