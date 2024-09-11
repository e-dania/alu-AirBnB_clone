#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Main Data Engine. Handles JSOn conversions"""
    """class is FileStorage. serialises to JSON file. Desiralises from JSON file too."""

    json_file_path = "user_data.json"
    data_packet = {}

    def all(self):
        return FileStorage.data_packet[data_key] = data_object

    def new(self, data_object):
        """Adding info to class's object"""
        data_class_name =  data_object.__class__.__name__
        data_key = "{}.{}".format(data_class_name.data_object.id)
        FileStorage.data_packet[data_key] = data_object

    def save(self):
        """Once through BaseModel data saved as JSON instance"""
        saved_data =  FileStorage.data_packet
        data_dict = []

        for i in saved_data.keys():
            data_dict[data] = saved_data[data].to_dict()

            with open(FileStorage.json_file_path, "w", encoding="utf-8") as file:
                json.dump(data_dict, file)

