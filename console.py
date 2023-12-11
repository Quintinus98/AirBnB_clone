#!/usr/bin/python3
"""Console - Inherits from cmd"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Represents the console shell"""
    prompt = "(hbnb) "
    file = None
    models = {"BaseModel": BaseModel()}

    def do_EOF(self, arg):
        """EOF reached
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Empty line + Enter shouldn't execute anything
        """
        print("", end="")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in self.models.keys():
            print("** class doesn't exist **")
        else:
            obj = models[args]
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in self.models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_files = storage.all()
            key = '{}.{}'.format(args[0], args[1])
        try:
            value = all_files[key]
        except KeyError:
            print("** no instance found **")
        else:
            print(value)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in self.models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_files = storage.all()
            key = '{}.{}'.format(args[0], args[1])
        try:
            del all_files[key]
        except KeyError:
            print("** no instance found **")
        else:
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all.
        """
        my_ls = []
        all_files = storage.all()
        if len(arg) == 0:
            for fs in all_files.values():
                my_ls.append(fs.__str__())
            print("{}".format(my_ls))
        elif arg not in self.models.keys():
            print("** class doesn't exist **")
        else:
            for v in all_files.values():
                if v["__class__"] == arg:
                    my_ls.append(v.__str__())
            print("{}".format(my_ls))

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = arg.split()
        all_files = storage.all()
        if args == []:
            print("** class name missing **")
        elif args[0] not in self.models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif '{}.{}'.format(args[0], args[1]) not in all_files.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            if args[2] not in ["id", "created_at", "updated_at"]:
                all_files[key][args[2]] = (args[3]).replace('"', '')
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
