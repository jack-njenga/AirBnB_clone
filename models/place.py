#!/usr/bin/python3


"""
Module place
Class that defines a staying location, including several details
that will be of interest to the customer such as number of rooms
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Place Class, inherits BaseModel

    Attributes:
        city_id (str)
        user_id (str)
        name (str)
        description (str)
        number_rooms (int)
        number_bathrooms (int)
        max_guest (int)
        price_by_night (int)
        latitude (float)
        longitude (float)
        amenity_ids ([str])
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialization

        args (any):

        kwargs (dict): Used when updating obj
        """
        super().__init__(*args, **kwargs)
        for key, value in kwargs.items():
            if key not in ["__class__", "created_at", "updated_at", "id"]:
                self.__dict__[key] = value
