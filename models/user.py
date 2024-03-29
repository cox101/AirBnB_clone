#!/usr/bin/python3
"""The Class user that inherits from base model"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for User"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

