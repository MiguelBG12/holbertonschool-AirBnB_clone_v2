#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This class manages databases of hbnb models """
    __engine = None
    __session = None

    def __init__(self):
        """ Connect the motor of the database """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}/{database}",
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a list of objects, optionally filtered by class."""
        db = {}
        all_classes = ['User', 'Review', 'Place', 'City', 'State']
        if cls is None:
            for kls in all_classes:
                kls = eval(kls)
                for new_instance in self.__session.query(kls).all():
                    key = new_instance.__class__.__name__
                    + '.' + new_instance.id
                    db[key] = new_instance
        else:
            for new_instance in self.__session.query(cls).all():
                key = new_instance.__class__.__name__ + '.' + new_instance.id
                db[key] = new_instance
        return db

    def new(self, obj):
        """Adds new object to db_storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves database dictionary"""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove object if exists."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary"""
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """ Log out of the database """
        self.__session.close()