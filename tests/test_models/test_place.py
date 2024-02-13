#!/usr/bin/python3

""" The unit test place """

import unittest
import models
import os
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(Place.__doc__, "Class Place has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_executable, "File place.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        place = Place()
        self.assertIsInstance(place, Place, "Object is not an instance of Place")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        place = Place()
        self.assertEqual(str(place), "[Place] ({}) {}".format(place.id, place.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        place = Place()
        first_updated = place.updated_at
        place.save()
        second_updated = place.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(place_dict['__class__'], 'Place', "Class name not included in dictionary")
        self.assertIsInstance(place_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(place_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
