#!/usr/bin/python3
""" testfile"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pep8
import unittest


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py',
                                        'models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_Place(test_basemodel):
    """test"""

    def __init__(self, *args, **kwargs):
        """test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_place_ids(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.place_ids), list)

    def tearDown(cls):
        """test"""
        del cls

    def test_is_subclass_Place(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_to_dict(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_doc_string(self):
        """test"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """test"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)

if __name__ == "__main__":
    unittest.main()
