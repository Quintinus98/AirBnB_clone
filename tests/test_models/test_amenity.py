#!/usr/bin/python3
"""Defines unittests for models/Amenity.py.
Unittest classes:
    TestAmenity
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_created(self):
        u = Amenity()
        key = '{}.{}'.format(u.__class__.__name__, u.id)
        self.assertIn(key, models.storage.all().keys())

    def test_id_is_public(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public(self):
        self.assertEqual(str, type(Amenity.name))

    def test_Amenitys_unique_ids(self):
        u1 = Amenity()
        u2 = Amenity()
        self.assertNotEqual(u1.id, u2.id)

    def test_Amenitys_diff_created_at(self):
        u1 = Amenity()
        sleep(0.05)
        u2 = Amenity()
        self.assertLess(u1.created_at, u2.created_at)

    def test_Amenitys_diff_updated_at(self):
        u1 = Amenity()
        sleep(0.05)
        u2 = Amenity()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_repr(self):
        date = datetime.today()
        dt_repr = repr(date)
        u = Amenity()
        u.id = "123456"
        u.created_at = u.updated_at = date
        ustr = u.__str__()
        self.assertIn("[Amenity] (123456)", ustr)
        self.assertIn("'id': '123456'", ustr)
        self.assertIn("'created_at': " + dt_repr, ustr)
        self.assertIn("'updated_at': " + dt_repr, ustr)

    def test_args_not_used(self):
        u = Amenity(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_init_with_kwargs(self):
        date = datetime.today()
        dt_iso = date.isoformat()
        u = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "345")
        self.assertEqual(u.created_at, date)
        self.assertEqual(u.updated_at, date)

    def test_instantiation_without_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        u = Amenity()
        sleep(0.05)
        created_at = u.created_at
        u.save()
        self.assertLess(created_at, u.updated_at)

    def test_save_with_args(self):
        u = Amenity()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_save_update_file(self):
        u = Amenity()
        u.save()
        uid = "Amenity.".format(u.id)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(uid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method"""

    def test_to_dict(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        u = Amenity()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())

    def test_to_dict_datetime_attributes_are_strings(self):
        u = Amenity()
        u_dict = u.to_dict()
        self.assertEqual(str, type(u_dict["id"]))
        self.assertEqual(str, type(u_dict["created_at"]))
        self.assertEqual(str, type(u_dict["updated_at"]))

    def test_to_dict_with_arguments(self):
        u = Amenity()
        with self.assertRaises(TypeError):
            u.to_dict(None)


if __name__ == "__main__":
    unittest.main()
