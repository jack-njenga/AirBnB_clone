#!/usr/bin/python3


"""
Module console
An administrative tool used to manage different aspects of the application
such as managing objects and their serialization/deserialization
"""

import cmd
import shlex
import re
from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNB management console class
    Manages objects and other actions of the project

    Inherits:
        cmd.Cmd: provides methods for managing a command line

    Attributes:
        prompt (str): prompt to display on each REPL step
        __models (dict): models objects supported in creation
        __completions (dict): autocomplete templates

    Methods:
        updateAutoComplete: update autocomplete templates on change

        do_quit, do_EOF, do_all, do_show, do_update,
        do_create, do_destroy, do_count
        completedefault
    """

    prompt = "(hbnb) "
    __models = {"BaseModel": base_model.BaseModel,
                "User": user.User,
                "State": state.State,
                "City": city.City,
                "Amenity": amenity.Amenity,
                "Place": place.Place,
                "Review": review.Review
                }
    __completions = {}

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.updateAutoComplete()

    def completedefault(self, text, line, begidx, endidx):
        """Override: Auto-complete all commands

        Attributes:
            text: The last argument in @line (separated by ' ')
            line: the whole text
            begidx: first index of text from beginning of line
            endidx: last index of text from beginning of line

        Returns:
            list of auto-complete string options
        """
        mline = line.partition(' ')[2]
        action = line.partition(' ')[0]
        offset = len(mline) - len(text)

        suggestions = []
        for suggestion in self.__completions[action]:
            if (suggestion.startswith(mline)):
                suggestions.append(suggestion[offset:])
        return suggestions

    def updateAutoComplete(self):
        """Generate and update auto-complete schema
        """
        objs = storage.all()
        actions = ["create", "destroy", "update", "all", "show", "count"]
        models = self.__models.keys()

        items = []
        for key in objs.keys():
            items.append(key.replace(".", " "))

        self.__completions["create"] = models
        self.__completions["all"] = models
        self.__completions["count"] = models
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

    def precmd(self, line):
        """Override: process line and allow for transformation

        Attributes:
            line: command string to process

        Returns:
            processed precmd string
        """
        command_re = r"(\w+)\.(\w+)\((.*)\)$"
        update_re = r"\"([^\"]+)\", (\{.+\})"
        classes = self.__models.keys()
        actions = ["all", "count", "show", "destroy", "update", "create"]
        matches = re.search(command_re, line)

        if (not matches):
            return cmd.Cmd.precmd(self, line)

        g = list(matches.groups())

        if (g[0] not in classes or g[1] not in actions):
            return cmd.Cmd.precmd(self, line)

        if (g[1] != "update"):
            line = f"{g[1]} {g[0]} {g[2]}".strip()
            return cmd.Cmd.precmd(self, line)

        matches = re.search(update_re, g[2])

        if (not matches):
            g[2] = ' '.join(g[2].split(",", 1))
            line = f"{g[1]} {g[0]} {g[2]}".strip()
            return cmd.Cmd.precmd(self, line)

        g_2 = list(matches.groups())
        _dict = eval(g_2[1])
        _cmds = []
        for k, v in _dict.items():
            _cmds.append(f"{g[1]} {g[0]} {g_2[0]} {k} {v}")

        if (not _cmds):
            line = f"{g[1]} {g[0]} {g_2[2]}".strip()
            return cmd.Cmd.precmd(self, line)

        self.cmdqueue = _cmds
        return cmd.Cmd.precmd(self, "")

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
            return False

        for obj in objs.values():
            if (obj.__class__.__name__ == args[0]):
                print(obj)

    def do_count(self, arg):
        """Count the number of occurrences of a class
        """
        args = shlex.split(arg)
        objs = storage.all()

        if (len(args) == 0):
            print(0)
            return False

        if (args[0] not in self.__models):
            print("** class doesn't exist **")
            return False

        count = 0
        for obj in objs.values():
            if (obj.__class__.__name__ == args[0]):
                count += 1

        print(count)

    def do_update(self, arg):
        """Update an instance of an object and save changes to file
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

    def emptyline(self):
        """Override: Do not repeat previous command on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
