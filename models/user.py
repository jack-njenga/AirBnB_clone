#!/usr/bin/python3

"""
This is the user class that inherits from BaseModel class.
"""
from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """
    User()

    attributes:
        email (str) : users email(empty string)
        password (str) : users password(empty string)
        first_name (str) : //
        last_name (str) : //

    usage:
        user.<attribte> = <attribute value>
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Intialization

        """
        super().__init__()

        if len(kwargs) > 0:
            base_list = list(BaseModel().__dict__.keys())
            base_list.append("__class__")

            for key in kwargs.keys():
                if key not in base_list:
                    self.__dict__[key] = kwargs[key]
