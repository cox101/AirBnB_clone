#!/usr/bin/python3
"""The Class Place that inherits from base model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Place"""
        super().__init__(*args, **kwargs)
        self.city_id = ""  # string - empty string: it will be the City.id
        self.user_id = ""  # string - empty string: it will be the User.id
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []  # list of string: it will be the list of Amenity.id

