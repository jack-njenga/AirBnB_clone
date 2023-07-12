#!/usr/bin/python3


"""
Module review
Class that defines the structure of a review for a Place,
including the main review content body and the User who made it
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review Class, inherits BaseModel

    Attributes:
        place_id (str)
        user_id (str)
        text (str)
    """

    place_id = ""
    user_id = ""
    text = ""

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
