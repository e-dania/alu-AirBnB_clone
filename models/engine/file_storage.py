#!/usr/bin/python3
"""File Storage ENGINE! handles the Data to and from JSON"""
from json import dump, load
from os.path import exists


class FileStorage:
   
    __file_path = "file.json"  
    __objects = {}  id

    def all(self):
      
        return FileStorage.__objects

    def new(self, obj):
       
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
       
        obj_dict = {key: value.to_dict() for key,
                    value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dump(obj_dict, f)

    def reload(self):
      
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded_dict = load(f)
                
                for key, value in loaded_dict.items():
                    class_name = key.split('.')[0]
                   
                    self.__objects[key] = eval(f"{class_name}(**value)")

    def reload(self):

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        file_name = FileStorage.__file_path
     
        if exists(file_name):
          
            with open(file_name) as f:
                obj_dict = load(f)
       
            for value in obj_dict.values():
               
                class_name = eval(value["__class__"])
                del value["__class__"]
               
                obj = class_name(**value)
                self.new(obj)
