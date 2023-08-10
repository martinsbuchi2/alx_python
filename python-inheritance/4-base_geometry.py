#!/usr/bin/python3
"""class BaseGeometry"""

class BaseGeometry:
    """base class"""
    
    def area(self):
        """public instance that reaise exception"""
        raise Exception("area() is not implemented")
    
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    