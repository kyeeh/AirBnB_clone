#!/usr/bin/python3
''' Module class State '''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class which inherits from BaseModel, public attributes:
    * name: empty string
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization point call to super class BaseModel '''
        super().__init__(*args, **kwargs)
