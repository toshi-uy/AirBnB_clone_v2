#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py',
                                        'models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_City(test_basemodel):
    """test city """

    def __init__(self, *args, **kwargs):
        """test city """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_is_subclass_City(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def tearDown(cls):
        """test"""
        del cls.city

    def tearDown(self):
        """test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_attributes(self):
        """test"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
