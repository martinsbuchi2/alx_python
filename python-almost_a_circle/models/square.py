"""Defines a Square class that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        
    @property
    def size(self):
        """Getter for size"""
        return self.width  # Since width and height are the same

    @size.setter
    def size(self, value):
        """Setter for size with width and height validation"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        
    