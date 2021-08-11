#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages stordatabasehbnb mod"""
    __engine = None
    __session = None

    def __init__(self):
        """inicialitation of class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        classes = [State, City, User]
        dictionary = {}
        if cls and cls in classes:
            for instance in self.__session.query(cls):
                key = str(cls.__class__.__name__) + '.' + str(instance.id)
                dictionary[key] = instance
        else:
            for i in classes:
                for instance in self.__session.query(i):
                    key = i.__name__ + '.' + str(instance.id)
                    dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_new = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session_reloaded = scoped_session(session_new)
        self.__session = Session_reloaded()
