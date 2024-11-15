#!/usr/bin/python3

from contextlib import ExitStack
from unittest.mock import patch
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from models import storage
from time import sleep
import os
import json
from console import HBNBCommand
from io import StringIO
import sys

# """Test handling of large amounts of data"""

# storage = FileStorage()
# model = BaseModel()
# models = [BaseModel() for _ in range(1000)]
# for model in models:
#     storage.new(model)
#     storage.save()

#     # Clear and reload
# FileStorage._FileStorage__objects = {}
# storage.reload()
# print(len(FileStorage._FileStorage__objects))


console = HBNBCommand()

"""Test help command"""
self = unittest.TestCase

# console.onecmd("help")
# temp_out = StringIO()
# sys.stdout = temp_out
# output = temp_out.getvalue()
# print(f"Output: {output}")
# self.assertIn("Documented commands", output)
# self.assertIn("EOF", output)
# self.assertIn("help", output)
# self.assertIn("quit", output)

# with patch('sys.stdout', new=StringIO()) as f:
#     console.onecmd("help")
#     output = f.getvalue()
#     print(f"Output: {output}")
#     self.assertIn("Documented commands", output)
#     self.assertIn("EOF", output)
#     self.assertIn("help", output)
#     self.assertIn("quit", output)


with ExitStack() as stack:
    stdout = stack.enter_context(patch('sys.stdout', new=StringIO()))
    stderr = stack.enter_context(patch('sys.stderr', new=StringIO()))
    console.onecmd("help")
    # Capture both stdout and stderr
    output = stdout.getvalue() + stderr.getvalue()
    self.assertIn("Documented commands", output)
    self.assertIn("EOF", output)
    self.assertIn("help", output)
    self.assertIn("quit", output)
