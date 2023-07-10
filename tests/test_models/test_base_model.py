#!/usr/bin/python3
"""
Unittest for BaseModelModel Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_base_model.py
"""

import unittest
import uuid
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for models/base_model.py"""

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        baseModel = BaseModel()
        id = baseModel.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (1000) cases"""
        N = 1000
        ids = sorted([BaseModel().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        baseModel = BaseModel()
        time_delta = datetime.datetime.now() - baseModel.created_at

        # Assert type
        self.assertIsInstance(datetime.datetime, baseModel.created_at)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        baseModel = BaseModel()
        time_delta = datetime.datetime.now() - baseModel.updated_at

        # Assert type
        self.assertIsInstance(datetime.datetime, baseModel.updated_at)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        baseModel = BaseModel()
        time_delta = baseModel.created_at - baseModel.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        baseModel = BaseModel()
        updated_at = baseModel.updated_at

        baseModel.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, baseModel.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        baseModel = BaseModel()
        id = baseModel.id

        baseModel.save()

        # instance id should be equal
        self.assertEqual(id, baseModel.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        baseModel = BaseModel()
        created_at = baseModel.created_at

        baseModel.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, baseModel.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        baseModel = BaseModel()
        _className = baseModel.__class__.__name__
        _id = baseModel.id
        _dict = baseModel.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) <{_dict}>",
                str(baseModel))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        baseModel = BaseModel()

        _dict = baseModel.__dict__.copy()
        _dict['__class__'] = baseModel.__class__.__name__
        _dict['created_at'] = baseModel.created_at.isoformat()
        _dict['updated_at'] = baseModel.updated_at.isoformat()

        base_model_dict = baseModel.to_dict()

        # Check if all keys are equal
        self.assertTrue(
                all((base_model_dict.get(k) == v for k, v in _dict.items())))
