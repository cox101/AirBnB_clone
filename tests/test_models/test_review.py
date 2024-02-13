#!/usr/bin/python3

""" The unit test review """

import unittest
import models
import os
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_docstring(self):
        """Test if module, class, methods, and functions have docstring"""
        self.assertIsNotNone(Review.__doc__, "Class Review has no docstring")

    def test_executable_file(self):
        """Test if file has executable permissions"""
        is_executable = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_executable, "File review.py does not have executable permissions")

    def test_init(self):
        """Test object initialization"""
        review = Review()
        self.assertIsInstance(review, Review, "Object is not an instance of Review")

    def test_id_unique(self):
        """Test uniqueness of ids"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id, "IDs are not unique")

    def test_str(self):
        """Test __str__ method"""
        review = Review()
        self.assertEqual(str(review), "[Review] ({}) {}".format(review.id, review.__dict__),
                         "__str__ method does not match the expected format")

    def test_save(self):
        """Test save method"""
        review = Review()
        first_updated = review.updated_at
        review.save()
        second_updated = review.updated_at
        self.assertNotEqual(first_updated, second_updated, "Updated time did not change after save")

    def test_to_dict(self):
        """Test to_dict method"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict, "to_dict() does not return a dictionary")
        self.assertEqual(review_dict['__class__'], 'Review', "Class name not included in dictionary")
        self.assertIsInstance(review_dict['created_at'], str, "created_at is not a string")
        self.assertIsInstance(review_dict['updated_at'], str, "updated_at is not a string")


if __name__ == '__main__':
    unittest.main()
