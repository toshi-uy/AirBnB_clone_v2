#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            lista = []
            dictionary = storage.all(City)
            for key, value in dictionary.items():
                if value.state_id == self.id:
                    lista.append(dictionary[key])
            return lista
