#!/usr/bin/python3
"""BaseModel - Defines all common attributes for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """Represents the Base Model for all common methods"""
    def __init__(self, *args, **kwargs):
        """Initializes the Base Model"""
        if (len(kwargs) != 0):
            self.create(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string doc"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            Update public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict containing all key/values"""
        attr = self.__dict__.copy()
        attr["__class__"] = self.__class__.__name__
        attr["created_at"] = self.created_at.isoformat()
        attr["updated_at"] = self.updated_at.isoformat()
        return attr

    def create(self, **kwargs):
        """Creates a BaseModel from a dictionary"""
        for k, v in kwargs.items():
            if k in ['created_at', 'updated_at']:
                v = datetime.fromisoformat(v)
            if k != '__class__':
                setattr(self, k, v)


if __name__ == "__main__":
    BaseModel()
