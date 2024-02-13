#!/usr/bin/python3
""" The unit test amenity """

import unittest
import models
import os
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ The test for class amenity"""
    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(Amenity.__doc__, "Class Amenity has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_executable, "File amenity.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity, "Object is not an instance of Amenity")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        amenity = Amenity()
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        amenity = Amenity()
        first_updated = amenity.updated_at
        amenity.save()
        second_updated = amenity.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(amenity_dict['__class__'], 'Amenity', "Class name not included in dictionary")
        self.assertIsInstance(amenity_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(amenity_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
