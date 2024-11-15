#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import shlex  # Fix for shlex undefined
from models import storage


class HBNBCommand(cmd.Cmd):
    """Holberton Bed & Breakfast (HBnB) Command Line class"""

    prompt = "(hbnb) "

    # Valid classes for the create command
    valid_classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.new(new_instance)  # Ensure the object is added to storage
            storage.save()  # Save changes to storage
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
