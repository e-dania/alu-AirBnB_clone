#!/usr/bin/python3

from uuid import uuid4 
from datetime import datetime
from models import storage

"""This Class file is the base clase for literally all core features"""
class BaseModel:
    """Base Model Class."""
    
    def __init__(self, *args, **kwargs):
        """Id(int), created_at, updated_at.Base Line Attributes."""

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns user objject in string format"""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updating saved data with data and time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary of object so it's saved. Using class attributes above"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
