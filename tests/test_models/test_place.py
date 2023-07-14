#!/usr/bin/python3


"""
Unittest for Place Class
Run from root folder with:
    python3 -m unittest tests/test_models/test_place.py
"""


import uuid
import datetime
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for models/place.py"""

    def test_inheritance(self):
        """Test: Place inherits from BaseModel"""
        place = Place()

        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_uuid_generated_and_str(self):
        """Test: UUID set in id field and is UUIDv4"""
        place = Place()
        id = place.id

        self.assertIsInstance(id, str)
        self.assertEqual(str(uuid.UUID(id)), id)

    def test_uuid_unique(self):
        """Test: UUIDS are unique for N (10) cases"""
        N = 10
        ids = sorted([Place().id for _ in range(0, N)])
        unique_ids = sorted(list(set(ids)))

        self.assertListEqual(ids, unique_ids)

    def test_created_at_set(self):
        """Test: created_at field set with current datetime"""
        place = Place()
        time_delta = datetime.datetime.now() - place.created_at

        # Assert type
        self.assertIsInstance(place.created_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_updated_at_set(self):
        """Test: updated_at field set with current datetime"""
        place = Place()
        time_delta = datetime.datetime.now() - place.updated_at

        # Assert type
        self.assertIsInstance(place.updated_at, datetime.datetime)
        # Difference within one second
        self.assertLessEqual(time_delta.seconds, 1)

    def test_created_at_updated_at_equal_on_new(self):
        """Test: created_at and updated_at are equal on new instance"""
        place = Place()
        time_delta = place.created_at - place.updated_at

        # No difference in time
        self.assertEqual(time_delta.microseconds, 0)

    def test_save(self):
        """Test: save method updates updated_at"""
        place = Place()
        updated_at = place.updated_at

        place.save()

        # instance updated_at should be different
        self.assertNotEqual(updated_at, place.updated_at)

    def test_id_not_modified_by_save(self):
        """Test: save method does not modify id"""
        place = Place()
        id = place.id

        place.save()

        # instance id should be equal
        self.assertEqual(id, place.id)

    def test_created_at_not_modified_by_save(self):
        """Test: save method does not modify created_at"""
        place = Place()
        created_at = place.created_at

        place.save()

        # instance updated_at should be equal
        self.assertEqual(created_at, place.created_at)

    def test_method___str__(self):
        """Test: check __str__() format"""
        place = Place()
        _className = place.__class__.__name__
        _id = place.id
        _dict = place.__dict__

        self.assertEqual(
                f"[{_className}] ({_id}) {_dict}",
                str(place))

    def test_method_to_dict(self):
        """Test: check dictionary output from to_dict()"""
        place = Place()

        _dict = place.__dict__.copy()
        _dict['__class__'] = place.__class__.__name__
        _dict['created_at'] = place.created_at.isoformat()
        _dict['updated_at'] = place.updated_at.isoformat()

        place_dict = place.to_dict()

        self.assertDictEqual(place_dict, _dict)

    def test_attributes_no_kwargs(self):
        """Test: Place attributes without arguments"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

        # test if attributes have been initialized to defaults
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertListEqual(place.amenity_ids, [])

    def test_attributes_with_kwargs(self):
        """Test: Place attributes when initialized"""
        my_dict = {
                "city_id": "ba5ec784-6bd0-4c26-858a-6a5a0d42dea0",
                "user_id": "7b85d78e-67d8-4fc8-b4fb-cd1bb733184e",
                "name": "Westend Estate",
                "description": "House F32",
                "number_rooms": 15,
                "number_bathrooms": 3,
                "max_guest": 5,
                "price_by_night": 200,
                "latitude": 32.325452,
                "longitude": -1.314533,
                "amenity_ids": ["a762a101-4142-4fba-8ddc-ced33ecf2047",
                                "efb53e7c-846d-455b-8f2a-761e2f2dc87d"]
                }

        place = Place(**my_dict)

        self.assertEqual(place.city_id, "ba5ec784-6bd0-4c26-858a-6a5a0d42dea0")
        self.assertEqual(place.user_id, "7b85d78e-67d8-4fc8-b4fb-cd1bb733184e")
        self.assertEqual(place.name, "Westend Estate")
        self.assertEqual(place.description, "House F32")
        self.assertEqual(place.number_rooms, 15)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 5)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 32.325452)
        self.assertEqual(place.longitude, -1.314533)
        self.assertListEqual(place.amenity_ids,
                             ["a762a101-4142-4fba-8ddc-ced33ecf2047",
                              "efb53e7c-846d-455b-8f2a-761e2f2dc87d"])
