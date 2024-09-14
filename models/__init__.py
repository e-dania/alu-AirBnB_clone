#!/usr/bin/python3
"""File to initialise all classes and
global spanning variables"""

from models.engine.file_storage import FileStorage

#Mention storage as this where all class data saved to.
storage = FileStorage()

#Load saved objects from file storage
storage.reload()
