#!/usr/bin/python3

"""
This is the user class that inherits from BaseModel class.
"""
from models.base_model import BaseModel


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
        super().__init__(*args, **kwargs)
        for key, value in kwargs.items():
            if key not in ["__class__", "created_at", "updated_at", "id"]:
                self.__dict__[key] = value
