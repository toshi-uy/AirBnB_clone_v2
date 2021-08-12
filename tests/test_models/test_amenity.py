#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py',
                                        'models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_Amenity(test_basemodel):
    """ test Amenity"""

    def __init__(self, *args, **kwargs):
        """ test init"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def tearDown(cls):
        """test"""
        del cls.amenity

    def tearDown(self):
        """test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_is_subclass_City(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_to_dict(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.amenity), True)

    def test_doc_string(self):
        """test"""
        self.assertIsNotNone(Amenity.__doc__)

    d