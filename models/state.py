#!/usr/bin/python3
"""Data for creating states/countries etc"""
from models.base_model import BaseModel

class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialsing empty arguments because initialisation needed"""
        super().__init(*args, **kwargs)