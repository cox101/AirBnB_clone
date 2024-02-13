#!/usr/bin/python3

""" The unit test state """

import unittest
import models
import os
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(State.__doc__, "Class State has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_executable, "File state.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        state = State()
        self.assertIsInstance(state, State, "Object is not an instance of State")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        state = State()
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        state = State()
        first_updated = state.updated_at
        state.save()
        second_updated = state.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(state_dict['__class__'], 'State', "Class name not included in dictionary")
        self.assertIsInstance(state_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(state_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
