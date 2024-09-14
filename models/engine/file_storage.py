#!/usr/bin/python3

from json import dump, load
from os.path import exists

"""File Storage ENGINE! handles the Data to and from JSON"""
class FileStorage:
     #Main Data Engine. Handles JSOn conversions"""
     #class is FileStorage. serialises to JSON file. Desiralises from JSON file too."""
    
    __file_path = "file.json" 
    __objects = {}  

    def all(self):
        # Returns dictionary containing all stored objects
        return FileStorage.__objects

    def new(self, obj):
        #Adding info to class's object
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        #Once through BaseModel data saved as JSON instance
        obj_dict = {key: value.to_dict() for key,
                    value in FileStorage.__objects.items()}
        # Writes the serialized data (as JSON) to the file
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dump(obj_dict, f)

    def reload(self):
        #Takes JSON to desiralise it (un-JSON-ify it when necessary)
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded_dict = load(f)

                # Reconstruct each object using the class name and data
                for key, value in loaded_dict.items():
                    class_name = key.split('.')[0]
                    # Extract class name from key
                    self.__objects[key] = eval(f"{class_name}(**value)")

    def reload(self):

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        # This is the dictionary we will be loading from the JSON file
        file_name = FileStorage.__file_path
        if exists(file_name):
            # Here open the file but as read only for serialisation
            with open(file_name) as f:
                obj_dict = load(f)
            for value in obj_dict.values():
                class_name = eval(value["__class__"])
                del value["__class__"]
                obj = class_name(**value)
                #Call on method above to iterate object to __objects
                self.new(obj)
