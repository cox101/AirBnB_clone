#!/usr/bin/python3
"""The Class review that inherits from base model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Review"""
        super().__init__(*args, **kwargs)
        self.place_id = ""  # it will be the Place.id
        self.user_id = ""  # it will be the User.id
        self.text = ""
