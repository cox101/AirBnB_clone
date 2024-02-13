#!/usr/bin/python3

""" The unit test for city """

import unittest
import models
import os
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(City.__doc__, "Class City has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/city.py', os.X_OK)
        self.assertTrue(is_executable, "File city.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        city = City()
        self.assertIsInstance(city, City, "Object is not an instance of City")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        city = City()
        self.assertEqual(str(city), "[City] ({}) {}".format(city.id, city.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        city = City()
        first_updated = city.updated_at
        city.save()
        second_updated = city.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(city_dict['__class__'], 'City', "Class name not included in dictionary")
        self.assertIsInstance(city_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(city_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
