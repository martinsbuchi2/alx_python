#!/usr/bin/python3

"""a class Square that defines a square"""
    
class Square:
    
    """instance attribute, then access and update private attribute"""
    
    def __init__(self, size):
        self.__size = size
        
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
   
    def area(self):
        return self.__size * self.__size