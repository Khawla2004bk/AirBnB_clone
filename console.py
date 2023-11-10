#!/usr/bin/python3
""" import modules """

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
""" HBNBCommand class"""


class HBNBCommand(cmd.Cmd):
    prompt = ""
    if sys.stdin.isatty() and sys.stdout.isatty():
        prompt = "(hbnb) "

    def do_EOF(self, line):
        "CTRL+D to exit the program"
        return True

    def do_quit(self, line):
        "Quit command to exit the program\n"
        return True

    def emptyline(self):
        """called when an empty line is entered by user"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
