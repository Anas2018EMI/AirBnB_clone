#!/usr/bin/python3
""" entry point of the command interpreter
    """
import cmd


class HBNBCommand(cmd.Cmd):
    """Holeberton Bed & Breakfast (HBNB) Command Line class

    Args:
        cmd (_type_): Python's simple framework for
        writing line-oriented command interpreters
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to
        the prompt.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
