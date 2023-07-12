#!/usr/bin/python3

"""
These are tests for City class
"""

from unittest import TestCase
from models.city import City
from models.base_model import BaseModel


class TestCity(TestCase):
    """
    Test:
        - Inheritance
        - Attributes
        - init
        - to_dict method
        - str repr
    """

    def test_Inheritance(self):
        """
        test for inheritance of the BaseModel class
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_Attributes(self):
        """
        test for correct attributes
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_init_attributes(self):
        """
        Test city when given args
        """
        city = City(state_id="254", name="Nairobi")
        self.assertEqual(city.state_id, "254")
        self.assertEqual(city.name, "Nairobi")

    def test_to_dict(self):
        """
        Test if to_dict method in BaseModel works
        """
        city = City()
        my_dict = city.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_str(self):
        """
        Test for str repr
        """
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
