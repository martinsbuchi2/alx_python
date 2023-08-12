#!/usr/bin/python3
"""
write metaclass from which the BaseGeometry
inherits.

NB: All class inherites from type class by 
default.
"""
class MyMetaClass(type):
    """the metaclass that inherits from the the 
       type class
    """
    def __dir__(cls) -> None:
        """write a method that remove '__init_subclass__
           from the dir() of the metaclass
        """
        attributes = super().__dir__()
        return [attrs for attrs in attributes if attrs != '__init_subclass__']
    

"""BaseGeometry"""
class BaseGeometry(metaclass = MyMetaClass):
    """subclass; BaseGeometry"""
    def __dir__(cls) -> None:
        """reomve __init_subclass__ from BaseGeometry"""
        attributes = super().__dir__()
        return [attrs for attrs in attributes if attrs != '__init_subclass__']
    
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle sub-class"""
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    
class Square(Rectangle):
    """square sub-class"""
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)