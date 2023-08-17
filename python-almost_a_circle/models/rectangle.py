"""Writing the class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class, which inherit the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle class"""
        super().__init__(id)  # Call Base class constructor with provided id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Returns the rectangle's width multiplied by its height."""
        return self.__height * self.__width
    
    def display(self):
        """Displays the Rectangle instance using '#' characters"""
        for _ in range(self.__height):
            print('#' * self.__width)