#!/usr/bin/python3
''' Module base_model which is the general structure '''
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    ''' BaseModel defines all common attributes/methods for other classes '''

    def __init__(self, *args, **kwargs):
        ''' constructor - initialize attributes of the class BaseModel '''
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'update_at']:
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

    def __str__(self):
        ''' magic function that prints class name, id and dictionary '''
        classname = self.__class__.__name__
        sid = self.id
        sdic = self.__dict__
        return "[{}] ({}) {}".format(classname, sid, sdic)

    def save(self):
        ''' updates \'updated_at\' with the current datetime '''
        self.update_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of dict
        add key named \'__class__\' with the name of the class
        format to isoformat() to methods created_at and update_at
        '''
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['update_at'] = self.update_at.isoformat()
        return new_dict
