import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extensions.database_enum import DataBase

file_path = os.path.abspath(os.getcwd())+"\database.db"

class DbConnectionHandler():
    """Sqlalchemy database connection"""

    def __init__(self,database: str):
        if(database == DataBase.MYSQL.value):
           self.__connection_string = "mysql+pymysql://root:telavita@mysql-db:3306/telavita"
        else:
            self.__connection_string = 'sqlite:///'+file_path
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :param - None
        :return - Engine connection database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string, echo = True)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()