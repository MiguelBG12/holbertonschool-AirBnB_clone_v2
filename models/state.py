#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """ Getter attribute cities for FileStorage """
            list_cities = []
            
            # Check if City class is defined in the models module
            if 'City' in dir(models):
                City = models.City

                # Filter cities with matching state_id
                list_cities = [city for city in models.storage.all(City).values() if city.state_id == self.id]

            return list_cities

