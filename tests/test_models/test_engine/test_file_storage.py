#!/usr/bin/python3

"""
This are Unittests for the FileStorage Class.
"""

import unittest
from models.engine import file_storage
from models.base_model import BaseModel
storage = file_storage.FileStorage()


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
        my_obj = storage.all().copy()
        base = BaseModel()
        base.my_number = 89
        storage.new(base)
        new = storage.all()
        self.assertEqual(len(new) - len(my_obj), 1)

    def test_reload(self):
        """
        Test for relod
        """
        storage.reload()
        count = len(storage.all())

        base = BaseModel()
        base.save()

        # update the storage
        storage.save()
        storage.reload()
        count_new = len(storage.all())
        self.assertEqual(count_new - count, 1)
