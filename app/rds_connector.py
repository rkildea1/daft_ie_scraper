from sqlalchemy import inspect
from sqlalchemy import create_engine
import pandas as pd
import variables as myvars
"""
Try to connect to a database
If the database exists, return the Ad_Links column as a list
If the database does not exist, return a blank list
"""

class SQLMANAGER:

    TABLENAME = myvars.RDSTABLENAME #default table name

    def __init__(self,engine):
        self.engine = engine

    def print_tables(self,engine):
        """
        Prints all the tables in the database
        """
        list_of_database_table_names = []
        engine = self.engine
        inspector = inspect(engine)
        tablenames = inspector.get_table_names()
        for tablename in tablenames:
            list_of_database_table_names.append(tablename)
        return list_of_database_table_names

    def return_scraped_urls_from_table(self, tablename_arg = TABLENAME):
        """
        Returns the scraped urls from a table
        Urls are returned in a list format from the column "Ad_link"
        If no match is found (table or column), blank list is returned
        """
        try:
            sql_db_column_name = f'{tablename_arg}."Ad_link"'
            sql = (f'select {sql_db_column_name} from {tablename_arg} ')
            df = pd.read_sql(sql,con=self.engine)   
            ad_link_column_as_list = df['Ad_link'].values
            return ad_link_column_as_list
        except:
            blanklist = []
            return blanklist


def connect_to_database():
    """
    Connects to the database
    """
    DATABASE_TYPE = 'postgresql'
    DBAPI = 'psycopg2'
    HOST = myvars.RDSHOST
    USER = myvars.RDSUSER
    PASSWORD = myvars.RDSPASS
    DATABASE = myvars.RDSDATABASENAME
    PORT = 5432
    engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    return engine.connect()    


def return_existing_db_urls():
    """
    Check the database and return the list of urls under the `Ad_Link` column as a pandas series
    """
    engine_connection = connect_to_database() #create the engine variable
    return SQLMANAGER.return_scraped_urls_from_table(engine_connection)

