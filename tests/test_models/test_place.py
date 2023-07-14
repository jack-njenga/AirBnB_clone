#!/usr/bin/python3

"""
These are tests for the Place class
"""
from unittest import TestCase
from models.place import Place
from models.base_model import BaseModel


class TestPlace(TestCase):
    """
    Test:
        - Inheritance
        - Attributes
        - Attributes types
        - initialization_with_args
        - to_dict method
        - str repr
    """
    def test_Inheritance(self):
        """
        Test for Inheritace
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_Attributes(self):
        """
        Test for Attributes
        (without args)
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_Attributes_types(self):
        """
        Test fot Attributes types
        (without args)
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(type(place.number_rooms), int)

        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(type(place.number_bathrooms), int)

        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(type(place.max_guest), int)

        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(type(place.price_by_night), int)

        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(type(place.latitude), float)

        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(type(place.longitude), float)

        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(type(place.amenity_ids), list)

    def test_place_initialization_with_args(self):
        """
        Test for initialization wuth *args
        (with **kwargs)
        """
        amenits = ["wifi", "swimming pool", "free parking"]
        place = Place(
                city_id="123",
                user_id="456",
                name="Nairobi Kenya",
                description="A place in Africa",
                number_rooms=5,
                number_bathrooms=5,
                max_guest=10,
                price_by_night=1000,
                latitude=17.72,
                longitude=-73.12,
                amenity_ids=amenits
                )
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Nairobi Kenya")
        self.assertEqual(place.description, "A place in Africa")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 5)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 1000)
        self.assertEqual(place.latitude, 17.72)
        self.assertEqual(place.longitude, -73.12)
        self.assertEqual(place.amenity_ids, amenits)

    def test_to_dict(self):
        """
        Test if to_dict method of the BaseModel class works
        """
        place = Place()
        my_dict = place.to_dict()
        self.assertEqual(type(my_dict), dict)

    def test_str(self):
        """
        Test for str repr
        """
        place = Place()
        strr = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(strr, str(place))
