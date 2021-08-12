#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py',
                                        'models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_User(test_basemodel):
    """test"""

    def __init__(self, *args, **kwargs):
        """test"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def tearDown(cls):
        """test"""
        del cls.user

    def tearDown(self):
        """test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_is_subclass_User(self):
        """ test subclass"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_to_dict(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_doc_string(self):
        """test"""
        self.assertIsNotNone(User.__doc__)
