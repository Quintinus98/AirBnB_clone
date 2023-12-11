#!/usr/bin/python3
"""Unittests for file_storage"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Represents the unittest for file_storage"""

    def test_file_type(self):
        """Test file type"""
        self.assertTrue(type(FileStorage()), FileStorage)

    def test_all(self):
        """test Filestorage all method"""
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """test Filestorage new method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn("BaseModel.{}".format(base.id), storage.all().keys())

    def test_save(self):
        """test Filestorage save method"""
        base = BaseModel()
        storage.new(base)
        storage.save()
        text = ""
        with open("file.json", "r", encoding="utf-8") as a_file:
            text = a_file.read()
            self.assertIn("BaseModel.{}".format(base.id), text)

    def test_reload(self):
        """Reloads the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w", encoding="utf-8") as a_file:
            a_file.write("{}")
        with open("file.json", "r", encoding="utf-8") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)

    @classmethod
    def tearDown(self):
        """Tears down the created file.json"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
