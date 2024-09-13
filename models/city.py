#!/usr/bin/python3
"""Class for city data"""

from models.base_model import BaseModel

class City(BaseModel):
    """Class for the city data"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialsing empty arguments because initialisation needed"""
        super().__init(*args, **kwargs)