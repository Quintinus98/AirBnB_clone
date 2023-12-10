#!/usr/bin/python3
"""Console - Inherits from cmd"""

import json
import cmd
import sys
from models.base_model import BaseModel
from models import storage


models = {"BaseModel": BaseModel()}

class HBNBCommand(cmd.Cmd): 
  """Represents the console shell"""
  prompt = "(hbtn) "
  file = None

  def do_EOF(self, arg):
    """EOF reached
    """
    return True
  
  def do_quit(self, arg):
    """Quit command to exit the program
    """
    sys.exit()

  def emptyline(self):
    print("", end="")

  def do_create(self, args):
    """
    Creates a new instance of BaseModel, saves it
    (to the JSON file) and prints the id
    """
    if len(args) == 0:
      print("** class name missing **")
    elif args not in models.keys():
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
    elif args[0] not in models.keys():
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
    elif args[0] not in models.keys():
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
    elif arg not in models.keys():
      print("** class doesn't exist **")
    else:
      for k, v in all_files.items():
        if k[:9] == arg:
          my_ls.append(v.__str__())
      print("{}".format(my_ls))


if __name__ == "__main__":
  HBNBCommand().cmdloop()
