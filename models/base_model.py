#!/usr/bin/python3


"""
This is the BaseModel class that that
defines all common attributes/methods for other classes.
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Base Model class

    attributes:
        id
        created_at
        updated_at
    methods:
        __str__
        save
        to_dict
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization

        args (any):

        kwargs (dict): Used when updating obj

        """
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            tm = datetime.now()
            self.created_at = tm
            self.updated_at = tm

    def __str__(self):
        """
        Returns the string representation
        of the an obj.
        """
        # print(self.__dict__)
        name = self.__class__.__name__
        dct = "[{}] ({}) {}".format(name, self.id, self.__dict__)

        return dct

    def save(self):
        """
        Updates the public instance attribute
        "updated_at" with the current datetime.
        """
        tm = datetime.now()
        self.updated_at = tm

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
