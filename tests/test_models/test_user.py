#!/usr/bin/python3

"""
This file contans tests for the User class
"""
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    tests:
        without args
        with ars
        inheritance
        string repr
    """
    def test_Attributes(self):
        """
        test for user without passing arguments
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

        # test if attributes have been initialized to ""
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_Attributes_with_args(self):
        """
        Test for user with arguments while initializing
        """
        # Arraging
        my_dict = {
                "email": "airbnb@gmail.com",
                "password": "airbnb1234",
                "first_name": "air",
                "last_name": "bnb"
                }

        # Act
        user = User(**my_dict)

        # Assert
        self.assertEqual(user.email, "airbnb@gmail.com")
        self.assertEqual(user.password, "airbnb1234")
        self.assertEqual(user.first_name, "air")
        self.assertEqual(user.last_name, "bnb")

    def test_Inheritance(self):
        """
        test for inheritance of the BaseModel class
        """
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_str(self):
        """
        Test the str return values
        """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
