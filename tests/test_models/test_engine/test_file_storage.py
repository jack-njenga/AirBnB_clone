#!/usr/bin/python3

"""
This are Unittests for the FileStorage Class.
"""

import unittest
import os
from models.engine import file_storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases:
        Test for new
        Test for save
        Test for reload
    """

    @classmethod
    def setUpClass(cls):
        """Set up tests"""
        cls.errors = ["** class name missing **\n",
                      "** class doesn't exist **\n",
                      "** instance id missing **\n",
                      "** no instance found **\n",
                      "** attribute name missing **\n",
                      "** value missing **\n"]
        cls.classes = ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]
        try:
            os.remove("file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_new(self):
        """
        Test if new adds objects
        (it should increase by one)
        """
        storage = file_storage.FileStorage()
        my_obj = storage.all().copy()
        base = BaseModel()
        base.my_number = 89
        storage.new(base)
        new = storage.all()
        self.assertEqual(len(new) - len(my_obj), 1)

    def test_save(self):
        """
        Test for save
        """
        storage = file_storage.FileStorage()
        storage.reload()
        count = len(storage.all())

        base = BaseModel()
        base.save()

        # update the storage
        storage.save()
        storage.reload()
        count_new = len(storage.all())
        self.assertEqual(count_new - count, 0)

    def test_reload(self):
        """
        Test for reload
        """
        storage = file_storage.FileStorage()
        storage.reload()
        count = len(storage.all())

        base = BaseModel()
        base.save()

        # update the storage
        storage.save()
        storage.reload()
        count_new = len(storage.all())
        self.assertEqual(count_new - count, 0)
