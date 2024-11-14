#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file to instances:

    """
import json
import models
from os.path import isfile


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file
    to instances:

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects

        Returns:
            dict: _description_
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): _description_
        """
        # print("tst")
        # print(obj.id)
        # print(f"{obj.__class__.__name__}")
        # print(obj)
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        # print(self.__objects)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        d1 = dict()
        for obj_id in self.__objects.keys():
            d1[obj_id] = self.__objects[obj_id].to_dict()
        with open(self.__file_path, mode="w") as file:
            json.dump(d1, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist, no exception should be raised)
        """
        # print(isfile(self.__file_path))
        if isfile(self.__file_path):
            with open(self.__file_path, mode="r") as file:
                data = json.load(file)
            for id, el in data.items():
                instance = models.BaseModel(**el)
                self.__objects[id] = instance
