#!/usr/bin/python3
''' Module class amenity.py '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    class Amenity that inherits from BaseModel, public class attributes:
    * name: empty string
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization point inherit super class '''
        super().__init__(*args, **kwargs)
