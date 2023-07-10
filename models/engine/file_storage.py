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

    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        from ..base_model import BaseModel
        return {k: BaseModel(**v) for k, v in self.__objects}

    def new(self, obj):
        """
        Sets in __objects a new value obj

        Args:
            obj(BaseModel): object to save in dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to JSON and save to __file_path
        """
        print("Saving", self.__objects)
        with open(self.__file_path, "w+") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes to __objects JSON from __file_path
        """
        if (path.exists(self.__file_path)):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
