#!/usr/bin/python3


"""
Unittest for Review Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_review.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for models/review.py"""

    def test_inheritance(self):
        """Test: Review inherits from BaseModel"""
        review = Review()

        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        review = Review()
        id = review.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([Review().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        review = Review()
        time_delta = datetime.datetime.now() - review.created_at

        # Assert type
        self.assertIsInstance(review.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        review = Review()
        time_delta = datetime.datetime.now() - review.updated_at

        # Assert type
        self.assertIsInstance(review.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        review = Review()
        time_delta = review.created_at - review.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        review = Review()
        updated_at = review.updated_at

        review.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, review.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        review = Review()
        id = review.id

        review.save()

        # instance id should be equal
        self.assertEqual(id, review.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        review = Review()
        created_at = review.created_at

        review.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, review.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        review = Review()
        _className = review.__class__.__name__
        _id = review.id
        _dict = review.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(review))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        review = Review()

        _dict = review.__dict__.copy()
        _dict['__class__'] = review.__class__.__name__
        _dict['created_at'] = review.created_at.isoformat()
        _dict['updated_at'] = review.updated_at.isoformat()

        review_dict = review.to_dict()

        self.assertDictEqual(review_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: Review attributes without arguments"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

        # test if attributes have been initialized to defaults
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes_with_kwargs(self):
        """Test: Review attributes when initialized"""
        my_dict = {
                "place_id": "ba5ec784-6bd0-4c26-858a-6a5a0d42dea0",
                "user_id": "ff670a8b-c443-445b-844e-e687dc50d225",
                "text": "Nice place, great neighbours."
                "A bit chilly for the summer, though.",
                }

        review = Review(**my_dict)

        self.assertEqual(review.place_id,
                         "ba5ec784-6bd0-4c26-858a-6a5a0d42dea0")
        self.assertEqual(review.user_id,
                         "ff670a8b-c443-445b-844e-e687dc50d225")
        self.assertEqual(review.text,
                         "Nice place, great neighbours."
                         "A bit chilly for the summer, though.")
