#!/usr/bin/python3
"""The Class state that inherits from base model"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class State that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for State"""
        super().__init__(*args, **kwargs)
        self.name = ""

