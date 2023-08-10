#!/usr/bin/python3
"""an empty class BaseGeometry"""

class BaseGeometry():
    """an empty class BaseGeometry"""
    pass

class HideInitSubclass(type):
    """hide init subclass"""
    def __dir__(self):
        attrs = super().__dir__()
        return [attr for attr in attrs if attr != '__init_subclass__']

class BaseGeometry(metaclass=HideInitSubclass):
    """hide init subclass"""
    pass

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))