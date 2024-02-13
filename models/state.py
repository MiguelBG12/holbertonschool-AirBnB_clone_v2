#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    from models.base_model import BaseModel, Base

    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

else:
    from models.base_model import BaseModel

    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            """Return the list of City objects linked to the current State"""
            city_list = []
            all_cities = models.storage.all("City")
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

