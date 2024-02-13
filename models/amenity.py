#!/usr/bin/python3

""" The class amenity that inherits from the base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity"""
        super().__init__(*args, **kwargs)
        self.name = ""
