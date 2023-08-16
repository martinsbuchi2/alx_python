# Python - Almost a circle

# Objectives:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# Tasks

1. Write the first class Base:
Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
Create a file named models/base.py:
 * Class Base:
    * private class attribute __nb_objects = 0
    * class constructor: def __init__(self, id=None)::
        * -if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
        * otherwise, increment __nb_objects and assign the new value to the public instance attribute id

2. Write the class Rectangle that inherits from Base
    * In the file models/rectangle.py
    * Class Rectangle inherits from Base
    * Private instance attributes, each with its own public getter and setter
            * __width -> width
            * __height -> height
            * __x -> x
            * __y -> y
    * Class constructor: def __init__(self, width, height, x=0, y=0, id=None)
            * Call the super class with id - this super call with use the logic of the __init__ of the Base class
            * Assign each argument width, height, x and y to the right attribute.

3. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
    * If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
    * If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
    * If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

4. Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
    * 1st argument should be the id attribute
    * 2nd argument should be the width attribute
    * 3rd argument should be the height   * attribute
    * 4th argument should be the x attribute
    * 5th argument should be the y attribute

9. 
mandatory
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
    * **kwargs can be thought of as a double pointer to a dictionary: key/value
        * As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
    * **kwargs must be skipped if *args exists and is not empty
    * Each key in this dictionary represents an attribute to the instance

    10. Write the class Square that inherits from Rectangle:

11. Update the class Square by adding the public getter and setter size
