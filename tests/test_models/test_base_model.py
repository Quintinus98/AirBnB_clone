#!/usr/bin/python3
"""Unittest for BaseModel"""

import models
import unittest
from models.base_model import BaseModel
from models import storage
from time import sleep
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Represents Unittest for BaseModel"""
    def test_create(self):
        base = BaseModel()
        key = '{}.{}'.format(base.__class__.__name__, base.id)
        self.assertIn(key, storage.all().keys())

    def test_create_unique(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_create_diff_times(self):
        base1 = BaseModel()
        sleep(0.5)
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)

    def test_str(self):
        date = repr(datetime.today())
        base = BaseModel()
        base.id = "12342-dla12"
        base.created_at = base.updated_at = date
        base_str = base.__str__()
        self.assertIn("[BaseModel] (12342-dla12)", base_str)
        self.assertIn("'id': '12342-dla12'", base_str)
        self.assertIn("'created_at': '{}'".format(date), base_str)
        self.assertIn("'updated_at': '{}'".format(date), base_str)

    def test_kwargs_instantiation(self):
        date = datetime.today()
        diso = date.isoformat()
        base = BaseModel(id="1323-lsd23", created_at=diso, updated_at=diso)
        self.assertEqual(base.id, "1323-lsd23")
        self.assertEqual(base.updated_at, date)
        self.assertEqual(base.created_at, date)

    def test_save_to_file(self):
        base = BaseModel()
        sleep(0.5)
        created_at = base.created_at
        base.save()
        self.assertLess(created_at, base.updated_at)

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict(self):
        self.assertTrue(dict, type(BaseModel().to_dict()))


if __name__ == "__main__":
    unittest.main()
