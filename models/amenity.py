#!/usr/bin/python3
"""Class for holding user "amenities" data"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to hold amenities related user data"""
    name = ""
