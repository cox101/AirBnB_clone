#!/usr/bin/python3

"""The Unit test BaseModel """

import unittest
import models
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(BaseModel.__doc__, "Class BaseModel has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_executable, "File base_model.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel, "Object is not an instance of BaseModel")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        base_model = BaseModel()
        self.assertEqual(str(base_model), "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        base_model = BaseModel()
        first_updated = base_model.updated_at
        base_model.save()
        second_updated = base_model.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(base_model_dict['__class__'], 'BaseModel', "Class name not included in dictionary")
        self.assertIsInstance(base_model_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(base_model_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
