#!/usr/bin/python3


"""
Unittest for User Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_user.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for models/user.py"""

    def test_inheritance(self):
        """Test: User inherits from BaseModel"""
        user = User()

        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        user = User()
        id = user.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([User().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        user = User()
        time_delta = datetime.datetime.now() - user.created_at

        # Assert type
        self.assertIsInstance(user.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        user = User()
        time_delta = datetime.datetime.now() - user.updated_at

        # Assert type
        self.assertIsInstance(user.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        user = User()
        time_delta = user.created_at - user.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        user = User()
        updated_at = user.updated_at

        user.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, user.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        user = User()
        id = user.id

        user.save()

        # instance id should be equal
        self.assertEqual(id, user.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        user = User()
        created_at = user.created_at

        user.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, user.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        user = User()
        _className = user.__class__.__name__
        _id = user.id
        _dict = user.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(user))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        user = User()

        _dict = user.__dict__.copy()
        _dict['__class__'] = user.__class__.__name__
        _dict['created_at'] = user.created_at.isoformat()
        _dict['updated_at'] = user.updated_at.isoformat()

        user_dict = user.to_dict()

        self.assertDictEqual(user_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: User attributes without arguments"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

        # test if attributes have been initialized to defaults
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_with_kwargs(self):
        """Test: User attributes when initialized"""
        my_dict = {
                "email": "airbnb@gmail.com",
                "password": "airbnb1234",
                "first_name": "air",
                "last_name": "bnb"
                }

        user = User(**my_dict)

        self.assertEqual(user.email, "airbnb@gmail.com")
        self.assertEqual(user.password, "airbnb1234")
        self.assertEqual(user.first_name, "air")
        self.assertEqual(user.last_name, "bnb")
