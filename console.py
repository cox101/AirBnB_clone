#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Usage: create <class>
        Create a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name and id (saves the change
        into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Prints all string representation of all instances based or not
        on the class name.
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg in storage.classes:
            print([str(obj) for key, obj in storage.all().items() if arg in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id by adding or updating
        attribute (saves the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        if len(args) == 4:
            attr_name = args[2]
            if hasattr(obj, attr_name):
                attr_value = args[3].strip('"')
                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** attribute doesn't exist **")
        else:
            print("Invalid number of arguments")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

