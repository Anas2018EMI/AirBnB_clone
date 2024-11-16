#!/usr/bin/python3
"""
Comprehensive unit tests for HBNBCommand console.
Tests all possible edge cases and scenarios.
"""

from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import unittest
import os
import pycodestyle


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand console"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_quit_command(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_empty_line(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_help_EOF(self):
        """Test help EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help EOF")
            self.assertIn("EOF", f.getvalue().strip())

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNotNone(console.__doc__, "console.py needs a docstring")
        self.assertGreaterEqual(len(console.__doc__), 50, "console.py docstring is too short")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__, "HBNBCommand class needs a docstring")
        self.assertGreaterEqual(len(HBNBCommand.__doc__), 50, "HBNBCommand class docstring is too short")


if __name__ == "__main__":
    unittest.main()
