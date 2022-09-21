from sqlalchemy import inspect
from sqlalchemy import create_engine
import pandas as pd
import variables.private_variables as myvars_private

"""
Try to connect to a database
If the database exists, return the Ad_Links column as a list

If the database does not exist, return a blank list
"""

def check_sql_for_links_already_crawled():

    
    sql_db_table_name = myvars.sql_db_table_name #RDS database table name you want to load or n if no db exists yet
    if sql_db_table_name != 'n':
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = myvars.HOST
        USER = (str(input('Please enter your RDS database username for checking : ')))
        PASSWORD = (str(input('Please enter the RDS database password')))
        DATABASE = myvars.databasename
        PORT = 5432
    else:
        pass
    try:
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        #testconnection
        engine.connect()
        # inspector = inspect(engine)
        sql_db_column_name = f'{sql_db_table_name}."Ad_link"'
        sql = (f'select {sql_db_column_name} from {sql_db_table_name} ')
        df = pd.read_sql(sql,con=engine)   
        list_of_db_stored_urls = df['Ad_link'].values
        return list_of_db_stored_urls
    except:
        blanklist = []
        return blanklist

