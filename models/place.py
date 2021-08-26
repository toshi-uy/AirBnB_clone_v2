#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import *
from sqlalchemy.orm import *
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from os import getenv

metadata = MetaData()
if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            lista = []
            dictionary = storage.all(self)
            for key, value in dictionary.items():
                if value.place_id == self.id:
                    lista.append(dictionary[key])
            return lista

        @property
        def amenities(self):
            """returns the list of Amenity instances"""
            return self.amenities

        @amenities.setter
        def amenities_setter(self, amenities=None):
            """setter of amenities"""
            if type(amenities) == Amenity:
                lista = []
                self.lista.append(amenities.id)
