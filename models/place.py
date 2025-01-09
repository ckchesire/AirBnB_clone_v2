#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
import models
from models.review import Review

class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place',
                           cascade='all, delete-orphan')
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE' != 'db'):
        @property
        def reviews(self):
            """Method to retrieve reviews
            """
            all_reviews = list(models.storage.all(Review).values())
            review_lst = [review for review in all_reviews 
                          if review.place_id == self.id]
            return review_lst