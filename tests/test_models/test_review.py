#!/usr/bin/python3
"""testfile """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8
import unittest


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py',
                                        'models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_review(test_basemodel):
    """test"""

    def __init__(self, *args, **kwargs):
        """test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def tearDown(cls):
        """test"""
        del cls.review

    def test_is_subclass_Review(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_to_dict(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_doc_string(self):
        """test"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """test"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('name' in self.review.__dict__)

if __name__ == "__main__":
    unittest.main()
