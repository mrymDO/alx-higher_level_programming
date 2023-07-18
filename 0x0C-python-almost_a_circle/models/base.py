#!/usr/bin/python3
"""
The module base.py defines the base class of other classes in the project
"""

import json
import os
import csv
import turtle


class Base():
    """ This class manage the id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        Args:
            id: id value to assign to the instance
            if not provided its value will be generated by __nb_objects counter
        """
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list) or not all(
                type(elem) == dict for elem in list_dictionaries):
            raise TypeError(
                        'list_dictionaries must be a list of dictionaries')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of list_objs to a file
        Args:
            list_objs: lis of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string representation json_string
        Args:
            json_string: a string representing a list of dictionaries
        """
        if json_string is None or json_string == '':
            return []
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            return None

        if new_instance is not None:
            new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_content = f.read()
            obj_list = cls.from_json_string(json_content)
            instances = []
            for obj_dict in obj_list:
                instance = cls.create(**obj_dict)
                instances.append(instance)
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format and saves it to a file"""
        if not isinstance(list_objs, list) and list_objs is not None:
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            if list_objs is not None:
                if cls.__name__ == 'Rectangle':
                    objects = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    objects = ['id', 'size', 'x', 'y']
                writer.writerow(objects)
                for obj in list_objs:
                    row = [str(getattr(obj, attr)) for attr in objects]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file. Returns list of instancees"""

        filename = cls.__name__ + ".csv"
        instances = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                objects = next(reader)
                for row in reader:
                    instance = cls(1, 1)
                    for attr, value in zip(objects, row):
                        setattr(instance, attr, int(value))
                    instances.append(instance)
        return instances