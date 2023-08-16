"""Writing the first class, Base with 
a private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
"""

class Base:
    """Base class for all classes in the project"""
    
    __nb_objects = 0 #private class attribute
    
    def __init__ (self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    