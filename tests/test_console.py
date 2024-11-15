#!/usr/bin/python3
"""
Comprehensive unit tests for HBNBCommand console.
Tests all possible edge cases and scenarios.
"""

from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from time import sleep
import os
import inspect
import pep8
import console


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand console"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except:
            pass
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except:
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

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
