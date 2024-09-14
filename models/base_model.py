#!/usr/bin/python3
"""This Class file is the base clase for literally all core features"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base Model Class."""

    def __init__(self, *args, **kwargs):
        """Id(int), created_at, updated_at.Base Line Attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            
            models.storage.new(self)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            

    def save(self):
        """updating saved data with data and time """
        self.update_time = datetime.now()
        self.storage.save()

    def to_dict(self):
        """returns dictionary of object so it's saved. Using class attributes above"""
        data_to_dict = self.__dict__.copy()
        data_to_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            data_to_dict[key] = value
        return data_to_dict

    def __str__(self):
        """Returns user objject in string format"""
        classname = f"[<{self.__class.__name__}>({self.id})] {self.__dict__}"
        return classname


class Trenches:
    """Using this to check an issue SMH dnt worry"""

    def __init__(self):
        return 0
