#!/usr/bin/python3


"""
Module console
An administrative tool used to manage different aspects of the application
such as managing objects and their serialization/deserialization
"""

import cmd
import shlex
from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNB management console class

    Inherits:
        cmd.Cmd: provides methods for managing a command line

    Attributes:
        prompt (str): prompt to display on each REPL step
        __models (dict): models objects supported in creation
        __completions (dict): autocomplete templates

    Methods:
        autocomplete: run autocomplete for any action
        updateAutoComplete: update autocomplete templates on change

        do_quit, do_EOF, do_all, do_show, do_update, do_create, do_destroy,
        complete_all, complete_show, complete_update, complete_create,
        complete_destroy
    """

    prompt = "(hbnb) "
    __models = {"BaseModel": base_model.BaseModel}
    __completions = {}

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.updateAutoComplete()

    def autocomplete(self, do, text, line):
        m = line.partition(' ')[2]
        offs = len(m) - len(text)
        return [s[offs:] for s in self.__completions[do] if s.startswith(m)]

    def updateAutoComplete(self):
        objs = storage.all()

        items = []
        for key in objs.keys():
            items.append(key.replace(".", " "))

        self.__completions["create"] = self.__models.keys()
        self.__completions["all"] = self.__models.keys()
        self.__completions["show"] = items
        self.__completions["destroy"] = items
        self.__completions["update"] = []

        ignore = ["id", "created_at", "updated_at", "__class__"]
        for item in items:
            id = item.replace(' ', '.')
            obj = objs[id].to_dict().copy()

            for v in ignore:
                del obj[v]

            if (len(obj.keys()) == 0):
                self.__completions["update"].append(item)
                continue
            for key in obj.keys():
                self.__completions["update"].append(f"{item} {key}")

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        print()
        return True

    def do_create(self, arg):
        """Create new instance of a class, saves and prints the id
        """
        args = shlex.split(arg)

        if (len(args) == 0):
            print("** class name missing **")
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")
            return False

        obj = self.__models.get(args[0])()
        print(obj.id)
        obj.save()

    def complete_create(self, text, line, begidx, endidx):
        """do_create auto-completions
        """
        return self.autocomplete("create", text, line)

    def do_show(self, arg):
        """Print string representation of all or named classes
        """
        args = shlex.split(arg)

        if (len(args) == 0):
            print("** class name missing **")
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")
            return False

        if (len(args) == 1):
            print("** instance id missing **")
            return False

        objs = storage.all()
        id = '.'.join([args[0], args[1]])

        if (id not in objs):
            print("** no instance found **")
            return False

        print(objs[id])

    def complete_show(self, text, line, begidx, endidx):
        """do_show auto-completions
        """
        return self.autocomplete("show", text, line)

    def do_destroy(self, arg):
        """Destroy an instance of an object and save changes to file
        """
        args = shlex.split(arg)

        if (len(args) == 0):
            print("** class name missing **")
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")
            return False

        if (len(args) == 1):
            print("** instance id missing **")
            return False

        objs = storage.all()
        id = '.'.join([args[0], args[1]])

        if (id not in objs):
            print("** no instance found **")
            return False

        del storage.objects[id]
        storage.save()
        self.updateAutoComplete()

    def complete_destroy(self, text, line, begidx, endidx):
        """do_show auto-completions
        """
        return self.autocomplete("destroy", text, line)

    def do_all(self, arg):
        """Print string representation of all or named classes
        """
        args = shlex.split(arg)
        objs = storage.all()

        if (len(args) == 0):
            for obj in objs.values():
                print(obj)
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")

        for obj in objs.values():
            if (obj.__class__.__name__ == args[0]):
                print(obj)

    def complete_all(self, text, line, begidx, endidx):
        """do_all auto-completions
        """
        return self.autocomplete("all", text, line)

    def do_update(self, arg):
        """Update an instance of an object and save changes to file
        """
        args = shlex.split(arg, posix=True)

        if (len(args) == 0):
            print("** class name missing **")
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")
            return False

        if (len(args) == 1):
            print("** instance id missing **")
            return False

        objs = storage.all()
        id = '.'.join([args[0], args[1]])

        if (id not in objs):
            print("** no instance found **")
            return False

        if (len(args) == 2):
            print("** attribute name missing **")
            return False

        if (len(args) == 3):
            print("** value missing **")
            return False

        # Try float
        if ('.' in args[3]):
            try:
                storage.objects[id][args[2]] = float(args[3])
            except Exception:
                pass
            else:
                storage.save()
                return False

        # Try int
        try:
            storage.objects[id][args[2]] = int(args[3])
        except Exception:
            pass
        else:
            storage.save()
            return False

        storage.objects[id][args[2]] = args[3]
        storage.save()

    def complete_update(self, text, line, begidx, endidx):
        """do_update auto-completions
        """
        return self.autocomplete("update", text, line)

    def emptyline(self):
        """override: Do not repeat previous command on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
