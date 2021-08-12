#!/usr/bin/python3
""" test file"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py',
                                        'models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_state(test_basemodel):
    """test"""

    def __init__(self, *args, **kwargs):
        """test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def tearDown(cls):
        """test"""
        del cls.state

    def tearDown(self):
        """test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_is_subclass_State(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_to_dict(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_doc_string(self):
        """test"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """test"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)
