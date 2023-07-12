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

        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key in kwargs.keys():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(kwargs[key], fmt)
                elif key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            super().__init__()
