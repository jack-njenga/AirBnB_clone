#!/usr/bin/python3

"""
These asr tests for the Amenity class
"""

from unittest import TestCase
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(TestCase):
    """
    Tests:
        - Inheritance
        - Attributes without args
        - Attriburtes with args
        - to_dict method
        - str repr
    """

    def test_Inheritance(self):
        """
        Test for inheritance of BaseModel class
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_Attributes(self):
        """
        Test for correct attributes
        (without args)

        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_Attributes_args(self):
        """
        Test for correct attributes
        (with args)

        """
        amenity = Amenity(name="airbnb")
        self.assertEqual(amenity.name, "airbnb")

    def test_to_dict(self):
        """
        Test if to_dict methon of BaseModel class works
        """
        amenity = Amenity()
        my_dict = amenity.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_str(self):
        """
        Test for str repr
        """
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
