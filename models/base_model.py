#!/usr/bin/python3
import datetime
import uuid
from engine.file_storage import FileStorage
class BaseModel:
    
    """Id(int), created_at, updated_at.Base Line Attributes."""
    def __init__(self, *args, **kwargs):
        """States all Class attributes and initialises them"""
        timePres = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for spec, value in kwargs.items():
                if spec == "__class__":
                    continue
                elif spec == "created_at" or spec == "updated_at":
                    setattr(self, spec, datetime.strptime(value, timePres))
                else:
                    setattr(self, spec, value)
        else:
            """id special here. uses uuid4 and converted to string"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.storage = FileStorage()


    def __str__(self):
        """Returns user objject in string format"""
        classname = f"[<{self.__class.__name__}>({self.id})] {self.__dict__}"
        return classname

    def save(self):
        """updating saved data with data and time """
        self.update_time = datetime.now()
        self.storage.save()

    def to_dict(self):
        """returns dictionary of object so it's saved. Using class attributes above"""
        data_to_dict = self.__dict__.copy()
        data_to_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            data_to_dict[key] = value

        return data_to_dict
    
if __name__ == "__main__":
    """Creating BaseModel Object then converts it into dictionary
    Once dictionary it is waits for potential serialization"""
    base_model = BaseModel();
    base_model.number = 12
    base_model.name = "FIRST DATA MODEL HERE"
    print(base_model)
    base_model.save()
    print(base_model)
    base_model_json = base_model.to_dict()
    print(base_model_json)
    print("JSON data version of original base model dude:")
    for spec in base_model_json.keys():
        print("\t{}: ({}) - {}".format(spec, type(base_model_json[spec]), base_model_json[spec]))
    else:
        print("None")

    



