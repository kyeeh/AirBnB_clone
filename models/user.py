#!/usr/bin/python3
''' Module class user.py '''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    class User that inherits from BaseModel, public class attributes:
    * email: empty string
    * password: empty string
    * first_name: empty string
    * last_name: empty string
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization point inherit super class '''
        super().__init__(*args, **kwargs)
