#!/usr/bin/python3

""" Class city that inherits from base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for City"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

