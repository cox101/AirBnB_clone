#!/usr/bin/python3

""" The FileStorage that serializes instances to a JSON file"""
"""" the deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON."""

    __file_path = "file.json"  # Path to the JSON file (e.g., file.json)
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    class_name = value['__class__']
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

