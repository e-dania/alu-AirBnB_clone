#!/usr/bin/python3
"""File Storage ENGINE! handles the Data to and from JSON"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Main Data Engine. Handles JSOn conversions"""
    """class is FileStorage. serialises to JSON file. Desiralises from JSON file too."""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """Adding info to class's object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        obj = self.__objects[key]

    def save(self):
        """Once through BaseModel data saved as JSON instance"""
        obj_dict = []

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):
        """Takes JSON to desiralise it (un-JSON-ify it when necessary)"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            None
