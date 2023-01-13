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
        return self.__dict__
