#!/usr/bin/python3
 """ The module models """

from models.engine.file_storage import FileStorage

"""Dictionary mapping class names to their corresponding module names"""

classes = {
    'BaseModel': 'BaseModel',
    'Amenity': 'Amenity',
    'State': 'State',
    'Place': 'Place',
    'Review': 'Review',
    'User': 'User'
}

""" Initialize a FileStorage instance and reload data"""
storage = FileStorage()
storage.reload()
