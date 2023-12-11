#!/usr/bin/python3
"""
  class FileStorage that serializes instances
  to a JSON file and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    Represents a FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    models = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        attr = {}
        for k, v in self.__objects.items():
            att[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as a_file:
            json.dump(self.__objects, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs = json.load(f)
            for k, v in objs.items():
                obj = self.models[v['__class__']](**v)
                self.__objects[k] = obj
