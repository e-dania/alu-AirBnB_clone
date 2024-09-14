#!/usr/bin/python3
"""Class to hold review data"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Variables for review Data"""
    place_id = ""
    user_id = ""
    text = ""
