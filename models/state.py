#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = getenv("HBNB_TYPE_STORAGE", default="fs")

        if self.storage == 'fs':
            @property
    
            def cities(self):
                """Return the list of City objects linked to the current State"""
                all_cities = models.storage.all()
                return [city for city in all_cities.values() if isinstance(city, models.City) and city.state_id == self.id]

        elif self.storage == 'db':
            cities = relationship('City', backref='state', cascade='all, delete')
