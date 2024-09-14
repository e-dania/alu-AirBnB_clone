#!/usr/bin/python3
"""This Class file is the base clase for literally all core features"""

from uuid import uuid4 as u4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class that defines common attributes and methods for other classes.
    Handles id generation, timestamps, and serialization.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs are provided, it updates attributes from the dictionary.
        Otherwise, it assigns new id, created_at, and updated_at attributes.
        """
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
