#!/usr/bin/python3

"""
This are Unittests for the FileStorage Class.
"""


import unittest
from models.engine import file_storage


class TestFileStorage(unittest.TestCase):
    """
    Test cases:
        Test for new
        Test for save
        Test for reload
    """

    def test_new(self):
        """
        Test if new adds objects
        (it should increase by one)
        """
        
        storage = FileStorage().all().copy()
        test = BaseModel()
        test.my_number = 89
        FileStorage().new(test)
        new = FileStorage().all()
        self.assertEqual(len(new) - len(storage), 1)

    def test_relod(self):
        """
        """
        pass
