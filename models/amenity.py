#!/usr/bin/python3

"""Class for holding user "amenities" data"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to hold amenities related user data"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialsing empty arguments because initialisation needed"""
        super().__init(*args, **kwargs)
