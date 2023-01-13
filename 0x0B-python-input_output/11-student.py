#!/usr/bin/python3
"""
    9-student: class Student
"""


class Student:
    """docstring for Student"""
    def __init__(self, first_name, last_name, age):
        """
            __init__ method
            Args:
                first_name (str): first name
                last_name (str): last name
                age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves json serializable dict
            format of object
        """
        dic = {}

        if attrs is None:
            return self.__dict__

        for att in attrs:
            if att in self.__dict__:
                dic[att] = self.__dict__[att]
        return dic

    def reload_from_json(self, json):
        """
            Loads python object from path
            Args:
                json: 'json str that contains
                python object
        """
        for key, value in json.item():
            if hasattr(self, key):
                setattr(self, key, value)
