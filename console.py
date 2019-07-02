#!/usr/bin/python3
''' Module class console.py '''
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_ls = {'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Place': Place, 'Review': Review}
store_all = models.storage.all()


class HBNBCommand(cmd.Cmd):
    ''' Class command interpreter HBNB '''

    def do_EOF(self, enter):
        ''' Close the command interpreter when you use the \'EOF\' command '''
        return True

    def do_quit(self, enter):
        ''' Close the command interpreter when you use the \'quit\' command '''
        return True

    def emptyline(self):
        ''' Clean the last nonempty command entered '''
        return False

    def do_create(self, args):
        ''' Create a new class including his id number '''
        if not args:
            print('** class name missing **')
        else:
            arg = args.split()
            if arg[0] in class_ls:
                exc = class_ls[arg[0]]()
                print(exc.id)
                exc.save()
            else:
                print('** class doesn\'t exist **')

    def do_show(self, args):
        ''' Print the object with id specified and his dictionary '''
        if not args:
            print('** class name missing **')
        else:
            arg = args.split()
            if not arg[0] in class_ls:
                print('** class doesn\'t exist **')
            else:
                if len(arg) > 1:
                    class_key = ''
                    class_key = arg[0] + '.' + arg[1]
                    if class_key in store_all:
                        print(store_all[class_key])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')

    def do_destroy(self, args):
        ''' Removes an object with id specified and his dictionary '''
        if not args:
            print('** class name missing **')
        else:
            arg = args.split()
            if not arg[0] in class_ls:
                print('** class doesn\'t exist **')
            else:
                if len(arg) > 1:
                    class_key = ''
                    class_key = arg[0] + '.' + arg[1]
                    if class_key in store_all:
                        store_all.pop(class_key)
                        models.storage.save()
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')

    def do_all(self, args):
        '''
        Prints all string representation of all instances
        based or not on the class name
        ex: \'(hbnb ) all\' or \'(hbnb )\' all BaseModel
        '''
        ls_val = []
        arg = args.split()
        if len(arg) == 0:
            for val in store_all.values():
                ls_val.append(str(val))
            print(ls_val)
        elif arg[0] in class_ls:
            for class_key in store_all:
                if arg[0] in class_key:
                    ls_val.append(str(store_all[class_key]))
            print(ls_val)
        else:
            print('** class doesn\'t exist **')

    def do_update(self, args):
        '''
        Updates an instance based on the class name and
        id by adding or updating attribute.
        ex: \'(hbnb )\' update BaseModel 123456789 attr_name attr_value
        '''
        arg = shlex.split(args)
        length = len(arg)
        if length == 0:
            print('** class name missing **')
            return
        if not arg[0] in class_ls:
            print('** class doesn\'t exist **')
            return
        else:
            if length == 1:
                print('** instance id missing **')
                return
            else:
                class_key = ''
                class_key = arg[0] + '.' + arg[1]
            if length == 2:
                print('** attribute name missing **')
                return
            if length == 3:
                print('** value missing **')
                return
            if length >= 4:
                if class_key in store_all:
                    setattr(store_all[class_key], arg[2], arg[3])
                    models.storage.save()
                else:
                    print('** no instance found **')
                    return


if __name__ == '__main__':
    HBNBCommand.prompt = '(hbnb) '
    HBNBCommand().cmdloop()
