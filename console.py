#!/usr/bin/python3

""" The Module Console """

import cmd
import shlex
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel, 'Amenity': Amenity,
        'State': State, 'Place': Place, 'Review': Review,
        'User': User, 'City': City
    }

    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if not argument:
            print("** class name missing **")
            return

        if argument not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[argument]()
        instance.save()
        print(instance.id)

    def do_show(self, argument):
        """string representation based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) < 1:
            print("** class name missing **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(tokens[0], tokens[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) < 1:
            print("** class name missing **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(tokens[0], tokens[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, argument):
        """all string representation of all instances"""
        objects = storage.all()
        if not argument:
            print([str(objects[obj]) for obj in objects])
        elif argument not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(objects[obj]) for obj in objects if
                   objects[obj].__class__.__name__ == argument])

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokens = shlex.split(argument)
        if len(tokens) < 1:
            print("** class name missing **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return
        elif len(tokens) < 3:
            print("** attribute name missing **")
            return
        elif len(tokens) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(tokens[0], tokens[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        obj = objects[key]
        setattr(obj, tokens[2], tokens[3])
        storage.save()

    def do_count(self, argument):
        """retrieve the number of instances of a class"""
        if not argument:
            print("** class name missing **")
            return

        if argument not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        count = sum(1 for obj in objects.values()
                    if obj.__class__.__name__ == argument)
        print(count)

    def precmd(self, line):
        """ executed just before the command line line is interpreted """
        if '.' in line:
            command, _class = line.split('.', 1)
            command = command.strip()
            _class, arguments = _class.split('(', 1)
            _class = _class.strip()
            arguments = arguments.rstrip(')')
            return "{} {} {}".format(command, _class, arguments)
        return line


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()

