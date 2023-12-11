#!/usr/bin/python3
"""Defines unittests for models/City.py.
Unittest classes:
    TestCity
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_type(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_created(self):
        u = City()
        key = '{}.{}'.format(u.__class__.__name__, u.id)
        self.assertIn(key, models.storage.all().keys())

    def test_id_is_public(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public(self):
        self.assertEqual(str, type(City.name))

    def test_state_id_is_public(self):
        self.assertEqual(str, type(City.state_id))

    def test_Citys_unique_ids(self):
        u1 = City()
        u2 = City()
        self.assertNotEqual(u1.id, u2.id)

    def test_Citys_diff_created_at(self):
        u1 = City()
        sleep(0.05)
        u2 = City()
        self.assertLess(u1.created_at, u2.created_at)

    def test_Citys_diff_updated_at(self):
        u1 = City()
        sleep(0.05)
        u2 = City()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_repr(self):
        date = datetime.today()
        dt_repr = repr(date)
        u = City()
        u.id = "123456"
        u.created_at = u.updated_at = date
        ustr = u.__str__()
        self.assertIn("[City] (123456)", ustr)
        self.assertIn("'id': '123456'", ustr)
        self.assertIn("'created_at': " + dt_repr, ustr)
        self.assertIn("'updated_at': " + dt_repr, ustr)

    def test_args_not_used(self):
        u = City(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_init_with_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        u = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "345")
        self.assertEqual(u.created_at, date)
        self.assertEqual(u.updated_at, date)

    def test_instantiation_without_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        u = City()
        sleep(0.05)
        created_at = u.created_at
        u.save()
        self.assertLess(created_at, u.updated_at)

    def test_save_with_args(self):
        u = City()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_save_update_file(self):
        u = City()
        u.save()
        uid = "City.".format(u.id)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(uid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method"""

    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        u = City()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())

    def test_to_dict_with_added_attributes(self):
        u = City()
        u.middle_name = "David"
        u.my_number = 1
        self.assertEqual("David", u.middle_name)
        self.assertIn("my_number", u.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        u = City()
        u_dict = u.to_dict()
        self.assertEqual(str, type(u_dict["id"]))
        self.assertEqual(str, type(u_dict["created_at"]))
        self.assertEqual(str, type(u_dict["updated_at"]))

    def test_to_dict_with_arguments(self):
        u = City()
        with self.assertRaises(TypeError):
            u.to_dict(None)


if __name__ == "__main__":
    unittest.main()
