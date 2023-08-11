#!/usr/bin/python3
"""BaseGeometry"""
class BaseGeometry:
    """Base class; reomve __init_subclass__"""
    def __dir__(cls) -> None:
    
        attributes = super().__dir__()
        
        list_to_return = []
        
        for attrs in attributes:
            if attrs != '__init_subclass__':
                list_to_return.append(attrs)
        return list_to_return
    
    
    #def __dir__(cls) -> None:
    #    attributes = super().__dir__()
        
     #   return [attributes for attributes in attributes if attributes != '__init_subclass__']