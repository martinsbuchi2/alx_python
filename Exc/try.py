"""my module"""
class Rectangle:
    
    """docstring for rectangle class."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        area = self.length * self.width
        return "The Area of a Rectangle with sides of length ({}) and width ({}) is {}".format (self.length , self.width, area)
    

my_area = Rectangle(34, 43)
my_area2 = Rectangle(35, 43)
my_area3 = Rectangle(34, 63)

print(my_area.Area())
print(my_area2.Area())
print(my_area3.Area())