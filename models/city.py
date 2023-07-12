#!/usr/bin/python3


"""
Module city
Class that defines a City, by name and e.g.
based on what State it is in
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    City Class, inherits BaseModel

    Attributes:
        state_id (str)
        name (str)
    """

    state_id = ""
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
