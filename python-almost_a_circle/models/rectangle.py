"""Writing the class Rectangle that inherits from Base"""
from base import Base

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
        """Setter for width"""
        self.__width = value
        
    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value
        
    
r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10) 
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)