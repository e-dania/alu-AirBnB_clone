#!/usr/bin/python3
"""
This contains the User class.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    This represents a User.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
