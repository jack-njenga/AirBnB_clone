#!/usr/bin/python3

"""
These are tests for the Review class
"""

from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review


class TestReview(TestCase):
    """
    Tests:
        - Inheritance
        - Attributes without **kwargs
        - Attributes with **kwargs
        - to_dict method
        - str repr
    """

    def test_Inheritance(self):
        """
        Test for review
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_Attributes(self):
        """
        Test for Attributes
        (without any arguments)
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_Attributes_args(self):
        """
        Test for Attributes
        (with **kwargs)
        """
        review = Review(
                place_id="254-Kenya",
                user_id="1234",
                text="Nothing to commit"
                )
        self.assertEqual(review.place_id, "254-Kenya")
        self.assertEqual(review.user_id, "1234")
        self.assertEqual(review.text, "Nothing to commit")

    def test_to_dict(self):
        """
        Test if to_dict method works
        """
        review = Review()
        my_dict = review.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_str(self):
        """
        Test for str repr
        """
        review = Review()
        strr = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), strr)
