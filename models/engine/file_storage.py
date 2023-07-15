#!/usr/bin/python3


"""
Module: file_storage
Manage serialization and deserialization of objects to files
"""


import json
from os import path


class FileStorage():
    """
    File Storage class

    attributes:
        __file_path
        __objects
    methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        """The file_path property."""
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    @property
    def objects(self):
        """The objects property."""
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value

    def all(self):
        """
        Returns the dictionary __objects
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        objs = {}

        for k, v in self.objects.copy().items():
            id = k.split(".")[0]
            if id == "BaseModel":
                objs[k] = BaseModel(**v)
            elif id == "User":
                objs[k] = User(**v)
            elif id == "State":
                objs[k] = State(**v)
            elif id == "City":
                objs[k] = City(**v)
            elif id == "Amenity":
                objs[k] = Amenity(**v)
            elif id == "Place":
                objs[k] = Place(**v)
            elif id == "Review":
                objs[k] = Review(**v)
        return objs

    def new(self, obj):
        """
        Sets in __objects a new value obj

        Args:
            obj(BaseModel): object to save in dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to JSON and save to __file_path
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.objects, f)

    def reload(self):
        """
        Deserializes to __objects JSON from __file_path
        """
        if (path.exists(self.__file_path)):
            with open(self.__file_path, "r") as f:
                obj = json.load(f)
                for key, value in obj.items():
                    self.objects[key] = value
