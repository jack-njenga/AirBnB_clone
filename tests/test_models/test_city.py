#!/usr/bin/python3


"""
Unittest for City Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_city.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for models/city.py"""

    def test_inheritance(self):
        """Test: City inherits from BaseModel"""
        city = City()

        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        city = City()
        id = city.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([City().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        city = City()
        time_delta = datetime.datetime.now() - city.created_at

        # Assert type
        self.assertIsInstance(city.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        city = City()
        time_delta = datetime.datetime.now() - city.updated_at

        # Assert type
        self.assertIsInstance(city.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        city = City()
        time_delta = city.created_at - city.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        city = City()
        updated_at = city.updated_at

        city.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, city.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        city = City()
        id = city.id

        city.save()

        # instance id should be equal
        self.assertEqual(id, city.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        city = City()
        created_at = city.created_at

        city.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, city.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        city = City()
        _className = city.__class__.__name__
        _id = city.id
        _dict = city.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(city))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        city = City()

        _dict = city.__dict__.copy()
        _dict['__class__'] = city.__class__.__name__
        _dict['created_at'] = city.created_at.isoformat()
        _dict['updated_at'] = city.updated_at.isoformat()

        city_dict = city.to_dict()

        self.assertDictEqual(city_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: City attributes without arguments"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

        # test if attributes have been initialized to defaults
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes_with_kwargs(self):
        """Test: City attributes when initialized"""
        my_dict = {
                "state_id": "dfcd0869-8e92-4855-84bc-44982aab95d1",
                "name": "Nairobi",
                }

        city = City(**my_dict)

        self.assertEqual(city.state_id, "dfcd0869-8e92-4855-84bc-44982aab95d1")
        self.assertEqual(city.name, "Nairobi")
