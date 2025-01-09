#!/usr/bin/python3
"""This module defines a class to manage database storage engine for hbnb clone
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Class to manage database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiating the database engine
        """
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')

        db_conn = "mysql+mysqldb://{}:{}@{}:3306/{}".format(username,
                                                            password,
                                                            host,
                                                            db_name)

        self.__engine = create_engine(db_conn, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to query current db session for all objects matching
           class name

           Return:
               Dictionary objects for specified class name or all objects
        """
        all_objs = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                all_objs = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                all_objs.extend(self.__session.query(subclass).all())
        dict_objs = {}
        for object in all_objs:
            key = "{}.{}".format(object.__class__.__name__, object.id)
            dict_objs[key] = object
        return dict_objs

    def new(self, obj):
        """Method is used to add an object to the current db session
        """
        self.__session.add(obj)

    def save(self):
        """Method used to commit transactions to the current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Method used to delete an  object from the current db session if
           object is not None
        """
        self.__session.delete(obj)

    def reload(self):
        """Method to ensure our database schema is synchronized with the
           defined alchemy models, when providing a new database session
        """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()
