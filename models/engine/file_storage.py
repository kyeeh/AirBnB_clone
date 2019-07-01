#!/usr/bin/python3
''' Module file_storage which create a class FileStorage '''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''
    class FileStorage that serializes instances to a JSON file
    deserializes JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Method that returns the private dictionary objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' Method which sets an object with the private attribute objects '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Method to serializes a private attribute objects to a JSON file '''
        dict_ob2 = {}
        for key, val in FileStorage.__objects.items():
            dict_ob2[key] = val.to_dict()
        with open('{}'.format(FileStorage.__file_path), 'w') as File:
            File.write(json.dumps(dict_ob2) + '\n')

    def reload(self):
        '''
        Method to deserializes a JSON file to an attribute __objects as:
        * BaseModel: BaseModel * User: User * State: State * City: city
        * Amenity: Amenity * Place: Place * Review: Review
        '''
        d_bs = {'BaseModel': BaseModel, 'User': User,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Place': Place, 'Review': Review}
        fl_sg = FileStorage.__objects
        try:
            with open('{}'.format(FileStorage.__file_path), 'r') as File:
                d_ob = json.load(File)
                for key in d_ob:
                    fl_sg[key] = d_bs[d_ob[key]['__class__']](**d_ob[key])
        except:
            pass
