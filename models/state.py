#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """

        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        from models.city import City
        cities = relationship("City", backref='state', cascade='all, delete')
else:
    class State(BaseModel):
        """ Use this option in case we use file_storage """
        name = ''

        @property
        def cities(self):
            from models.city import City
            new_cities = []
            for city in models.storage.all(City).values():
                if hasattr(city, 'state_id') and city.state_id == self.id:
                    new_cities.append(city)
            return new_cities