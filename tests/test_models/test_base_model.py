#!/usr/bin/python3
"""
Unittest for BaseModel Class
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
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([BaseModel().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        baseModel = BaseModel()
        time_delta = datetime.datetime.now() - baseModel.created_at

        # Assert type
        self.assertIsInstance(baseModel.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        baseModel = BaseModel()
        time_delta = datetime.datetime.now() - baseModel.updated_at

        # Assert type
        self.assertIsInstance(baseModel.updated_at, datetime.datetime)
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
                f"[{_className}] ({_id}) {_dict}",
                str(baseModel))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        baseModel = BaseModel()

        _dict = baseModel.__dict__.copy()
        _dict['__class__'] = baseModel.__class__.__name__
        _dict['created_at'] = baseModel.created_at.isoformat()
        _dict['updated_at'] = baseModel.updated_at.isoformat()

        base_model_dict = baseModel.to_dict()

        self.assertDictEqual(base_model_dict, _dict)

    def test_kwargs(self):
        """Test: object is created from kwargs dict"""
        baseModel1 = BaseModel()
        baseModel1.name = "Miles"
        baseModel1.my_number = 42

        baseModel1_dict = baseModel1.to_dict()

        baseModel2 = BaseModel(**baseModel1_dict)
        baseModel2_dict = baseModel2.to_dict()

        self.assertFalse(baseModel1 is baseModel2)
        self.assertDictEqual(baseModel1_dict, baseModel2_dict)

    def test_kwargs_if_None_or_empty(self):
        """Test: new instance if no kwargs dict"""
        baseModel1 = BaseModel()
        baseModel2 = BaseModel(None, None)
        baseModel3 = BaseModel(None, {})

        # Make sure UUIDs are different
        self.assertNotEqual(baseModel1.id, baseModel2.id)
        self.assertNotEqual(baseModel2.id, baseModel3.id)
        self.assertNotEqual(baseModel1.id, baseModel3.id)

        # Check created_at time incrementing
        self.assertLessEqual(baseModel1.created_at, baseModel2.created_at)
        self.assertLessEqual(baseModel2.created_at, baseModel3.created_at)
