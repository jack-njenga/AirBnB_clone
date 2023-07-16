#!/usr/bin/python3


"""
Module: file_storage
Manage serialization and deserialization of objects to files
"""

import json


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
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects a new value obj

        Args:
            obj(BaseModel): object to save in dictionary
        """
        name = obj.to_dict()["__class__"]
        i_d = obj.to_dict()["id"]

        key = name + "." + i_d
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON and save to __file_path
        """
        json_obj = {}
        self.reload()
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w+', encoding="utf-8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """
        Deserializes to __objects JSON from __file_path
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj = json.load(f)
            for key in obj.keys():
                self.__objects[key] = eval(obj[key]["__class__"])(**obj[key])
        except Exception:
            pass
