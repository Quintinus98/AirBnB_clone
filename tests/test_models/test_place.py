#!/usr/bin/python3
"""Defines unittests for models/Place.py.
Unittest classes:
    TestPlace
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_type(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_created(self):
        u = Place()
        key = '{}.{}'.format(u.__class__.__name__, u.id)
        self.assertIn(key, models.storage.all().keys())

    def test_id_is_public(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name_is_public(self):
        self.assertEqual(str, type(Place.name))

    def test_description_is_public(self):
        self.assertEqual(str, type(Place.description))

    def test_Places_unique_ids(self):
        u1 = Place()
        u2 = Place()
        self.assertNotEqual(u1.id, u2.id)

    def test_Places_diff_created_at(self):
        u1 = Place()
        sleep(0.05)
        u2 = Place()
        self.assertLess(u1.created_at, u2.created_at)

    def test_Places_diff_updated_at(self):
        u1 = Place()
        sleep(0.05)
        u2 = Place()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_repr(self):
        date = datetime.today()
        dt_repr = repr(date)
        u = Place()
        u.id = "123456"
        u.created_at = u.updated_at = date
        ustr = u.__str__()
        self.assertIn("[Place] (123456)", ustr)
        self.assertIn("'id': '123456'", ustr)
        self.assertIn("'created_at': " + dt_repr, ustr)
        self.assertIn("'updated_at': " + dt_repr, ustr)

    def test_args_not_used(self):
        u = Place(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_init_with_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        u = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "345")
        self.assertEqual(u.created_at, date)
        self.assertEqual(u.updated_at, date)

    def test_instantiation_without_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        u = Place()
        sleep(0.05)
        created_at = u.created_at
        u.save()
        self.assertLess(created_at, u.updated_at)

    def test_save_with_args(self):
        u = Place()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_save_update_file(self):
        u = Place()
        u.save()
        uid = "Place.".format(u.id)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(uid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method"""

    def test_to_dict(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        u = Place()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())

    def test_to_dict_with_added_attributes(self):
        u = Place()
        u.middle_name = "David"
        u.my_number = 1
        self.assertEqual("David", u.middle_name)
        self.assertIn("my_number", u.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        u = Place()
        u_dict = u.to_dict()
        self.assertEqual(str, type(u_dict["id"]))
        self.assertEqual(str, type(u_dict["created_at"]))
        self.assertEqual(str, type(u_dict["updated_at"]))

    def test_to_dict_with_arguments(self):
        u = Place()
        with self.assertRaises(TypeError):
            u.to_dict(None)


if __name__ == "__main__":
    unittest.main()
