#!/usr/bin/python3
"""class"""

class BaseGeometry:
    """base class"""
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherit class sub-class"""
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    