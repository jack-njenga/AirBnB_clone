#!/usr/bin/python3

"""
This are tests for State class
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests:
        - Inheritance
        - Attributes
        - to_dict
        - Str repr
    """
    def test_Inheritance(self):
        """
        Test for inheritance of BaseModel class
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_Attributes(self):
        """
        Test for correct attributes
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_dict_values(self):
        """
        Test for to_dict method of the BaseModel class
        """
        state = State()
        my_dict = state.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_str(self):
        """
        Test for str repr
        """
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))
