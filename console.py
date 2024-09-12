#!/usr/bin/python3
"""
This module contains the command interpreter.
"""

import cmd
from models.user import User
from models.file_storage import FileStorage

file_storage = FileStorage()

class HBNBCommand(cmd.Cmd):
    """
    This class represents the command interpreter.
    """

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new object.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name == "User":
            obj = User()
        else:
            print("** class doesn't exist **")
            return
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Shows an object.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        obj_id = args[1]
        if cls_name == "User":
            obj = file_storage.all(User).get(obj_id)
        else:
            print("** class doesn't exist **")
            return
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """
        Destroys an object.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        obj_id = args[1]
        if cls_name == "User":
            obj = file_storage.all(User).get(obj_id)
        else:
            print("** class doesn't exist **")
            return
        if obj is None:
            print("** no instance found **")
            return
        del file_storage.__objects[obj_id]
        file_storage.save()

    def do_update(self, arg):
        """
        Updates an object.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
