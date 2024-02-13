#!/usr/bin/python3

""" The unit test User """

import unittest
import models
import os
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(User.__doc__, "Class User has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_executable, "File user.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        user = User()
        self.assertIsInstance(user, User, "Object is not an instance of User")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        user = User()
        self.assertEqual(str(user), "[User] ({}) {}".format(user.id, user.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        user = User()
        first_updated = user.updated_at
        user.save()
        second_updated = user.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(user_dict['__class__'], 'User', "Class name not included in dictionary")
        self.assertIsInstance(user_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(user_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
