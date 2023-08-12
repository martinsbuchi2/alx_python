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