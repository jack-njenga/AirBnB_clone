#!/usr/bin/python3


"""
Module anemity
Class that defines an Amenity (facilities)
by name e.g. a gym
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class, inherits BaseModel

    Attributes:
        name (str)
    """

    name = ""

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
