#!/usr/bin/python3
"""
  class FileStorage that serializes instances
  to a JSON file and deserializes JSON file to instances
"""
import json
import os


class FileStorage():
    """
    Represents a FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as a_file:
            json.dump(self.__objects, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs = json.load(f)
            for k, v in objs.items():
                self.__objects[k] = v
