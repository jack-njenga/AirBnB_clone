#!/usr/bin/python3


"""
Unittest for State Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_state.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for models/state.py"""

    def test_inheritance(self):
        """Test: State inherits from BaseModel"""
        state = State()

        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        state = State()
        id = state.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([State().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        state = State()
        time_delta = datetime.datetime.now() - state.created_at

        # Assert type
        self.assertIsInstance(state.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        state = State()
        time_delta = datetime.datetime.now() - state.updated_at

        # Assert type
        self.assertIsInstance(state.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        state = State()
        time_delta = state.created_at - state.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        state = State()
        updated_at = state.updated_at

        state.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, state.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        state = State()
        id = state.id

        state.save()

        # instance id should be equal
        self.assertEqual(id, state.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        state = State()
        created_at = state.created_at

        state.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, state.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        state = State()
        _className = state.__class__.__name__
        _id = state.id
        _dict = state.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(state))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        state = State()

        _dict = state.__dict__.copy()
        _dict['__class__'] = state.__class__.__name__
        _dict['created_at'] = state.created_at.isoformat()
        _dict['updated_at'] = state.updated_at.isoformat()

        state_dict = state.to_dict()

        self.assertDictEqual(state_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: State attributes without arguments"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

        # test if attributes have been initialized to defaults
        self.assertEqual(state.name, "")

    def test_attributes_with_kwargs(self):
        """Test: State attributes when initialized"""
        my_dict = {
                "name": "Nairobi",
                }

        state = State(**my_dict)

        self.assertEqual(state.name, "Nairobi")
