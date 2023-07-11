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

        objs = {}

        for k, v in self.objects.copy().items():
            id = k.split(".")[0]
            match (id):
                case "BaseModel":
                    objs[k] = BaseModel(**v)
                case _:
                    pass
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
        with open(self.__file_path, "w+") as f:
            for key in self.__objects.keys():
                line = json.dumps({key: self.objects[key]})
                f.write(line + "\n")

    def reload(self):
        """
        Deserializes to __objects JSON from __file_path
        """
        if (path.exists(self.__file_path)):
            with open(self.__file_path, "r") as f:
                for line in f:
                    obj = json.loads(line)
                    key = list(obj.keys())[0]
                    value = obj.get(key)
                    self.objects[key] = value
