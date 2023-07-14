#!/usr/bin/python3

"""
These are tests for the HBNBCommand class(console.py)
"""

from unittest import TestCase
from console import HBNBCommand as Bnb
from unittest.mock import patch
from io import StringIO


class TestConsole(TestCase):
    """
    Tests:
        - Intialization
        - updateAutoComplete
        - quit
        - EOF
        - create
        - show
        - destroy
        - all
        - update
    """

    def test_init(self):
        """
        Test for init method
        """

        hbnb = Bnb()
        self.assertEqual(hbnb.prompt, "(hbnb) ")

    def test_updateAutoComplete(self):
        """
        Test for updateAutoComplete method
        """

        hbnb = Bnb()
        hbnb.updateAutoComplete()
        list_1 = list(hbnb._HBNBCommand__completions["create"])
        list_2 = list(hbnb._HBNBCommand__models.keys())
        self.assertEqual(list_1, list_2)

    def test_quit(self):
        """
        Test for quit command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(Bnb().onecmd("quit"))

    def test_eof(self):
        """
        Test for EOF command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(Bnb().onecmd("EOF"))

    def test_create(self):
        """
        Test for create method error output
        """

        err = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            Bnb().onecmd("create")
            self.assertEqual(f.getvalue(), err)
        pass

    def test_show(self):
        """
        Test for show error output
        """

        err = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            Bnb().onecmd("show City Nairobi")
            self.assertEqual(f.getvalue(), err)

    def test_destroy(self):
        """
        Test for destroy command error output
        """

        err = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            Bnb().onecmd("destroy City")
            self.assertEqual(f.getvalue(), err)

    def test_all(self):
        """
        Test for all command error output
        """

        err = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            Bnb().onecmd("all Mombasa")
            self.assertEqual(f.getvalue(), err)

    def test_update(self):
        """
        Test for update command error message
        """

        err = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            Bnb().onecmd("update User 007")
            self.assertEqual(f.getvalue(), err)
