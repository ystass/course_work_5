import psycopg2
from config import config


class DBManager:

    def get_companies_and_vacancies_count(self, params):
        conn = psycopg2.connect(dbname='courswork5', **params)
        with conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT employers.name, COUNT(vacancies.employer_id) AS vacancies_count 
                FROM employers 
                LEFT JOIN vacancies ON employers.id = vacancies.employer_id 
                GROUP BY employers.name''')
                companies_and_vacs_count = cur.fetchall()
                return companies_and_vacs_count
        conn.close()