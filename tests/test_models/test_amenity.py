#!/usr/bin/python3


"""
Unittest for Amenity Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_amenity.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for models/amenity.py"""

    def test_inheritance(self):
        """Test: Amenity inherits from BaseModel"""
        amenity = Amenity()

        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        amenity = Amenity()
        id = amenity.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([Amenity().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        amenity = Amenity()
        time_delta = datetime.datetime.now() - amenity.created_at

        # Assert type
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        amenity = Amenity()
        time_delta = datetime.datetime.now() - amenity.updated_at

        # Assert type
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        amenity = Amenity()
        time_delta = amenity.created_at - amenity.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        amenity = Amenity()
        updated_at = amenity.updated_at

        amenity.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, amenity.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        amenity = Amenity()
        id = amenity.id

        amenity.save()

        # instance id should be equal
        self.assertEqual(id, amenity.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        amenity = Amenity()
        created_at = amenity.created_at

        amenity.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, amenity.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        amenity = Amenity()
        _className = amenity.__class__.__name__
        _id = amenity.id
        _dict = amenity.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(amenity))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        amenity = Amenity()

        _dict = amenity.__dict__.copy()
        _dict['__class__'] = amenity.__class__.__name__
        _dict['created_at'] = amenity.created_at.isoformat()
        _dict['updated_at'] = amenity.updated_at.isoformat()

        amenity_dict = amenity.to_dict()

        self.assertDictEqual(amenity_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: Amenity attributes without arguments"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

        # test if attributes have been initialized to defaults
        self.assertEqual(amenity.name, "")

    def test_attributes_with_kwargs(self):
        """Test: Amenity attributes when initialized"""
        my_dict = {
                "name": "Gym",
                }

        amenity = Amenity(**my_dict)

        self.assertEqual(amenity.name, "Gym")
