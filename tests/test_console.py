#!/usr/bin/python3
"""
Tests for HBNBCommand Class
"""
import os
import unittest
import console
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test for HBNBCommand Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set HBNBCommand Class
        """
        cls.cli = HBNBCommand()

    @classmethod
    def teardown(cls):
        """
        Delete HBNBCommand Class
        """
        del cls.cli
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_BaseModel.__doc__)
        self.assertIsNotNone(HBNBCommand.do_User.__doc__)
        self.assertIsNotNone(HBNBCommand.do_State.__doc__)
        self.assertIsNotNone(HBNBCommand.do_City.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Amenity.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Place.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Review.__doc__)

    def test_init(self):
        """
        Check objects as instance of HBNBCommand
        """
        self.assertTrue(isinstance(self.cli, HBNBCommand))

    def test_quit(self):
        """
        Check quit command
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("quit")
            self.assertEqual('', output.getvalue())

    def test_emptyline(self):
        """
        Check empty line
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("\n")
            self.assertEqual('', output.getvalue())

    def test_create(self):
        """
        Check create command
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create")
            self.assertEqual("** class name missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create Paula")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create City")
            self.assertTrue(len(output.getvalue()) > 20)

    def test_show(self):
        """
        Check show command
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show")
            self.assertEqual("** class name missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show Paula")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show City")
            self.assertEqual("** instance id missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show City 37731-pqrs")
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_destroy(self):
        """
        Check destroy command
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy")
            self.assertEqual("** class name missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy Paula")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy City")
            self.assertEqual("** instance id missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy City 37731-pqrs")
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_all(self):
        """
        Check all command
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("all Paula")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("all City")
            self.assertTrue("[" in output.getvalue())
            self.assertTrue("]\n" in output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("City.all()")
            self.assertTrue("[" in output.getvalue())
            self.assertTrue("]\n" in output.getvalue())

if __name__ == "__main__":
    unittest.main()
