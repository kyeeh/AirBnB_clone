#!/usr/bin/python3
"""
Tests for BaseModel Class
"""
import os
import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set Base Model Class
        """
        cls.bm = BaseModel()
        cls.bm.name = "CLI"
        cls.bm.num = 73

    @classmethod
    def teardown(cls):
        """
        Delete Base Model Class
        """
        del cls.bm
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """
        Check pep8
        """
        psg = pep8.StyleGuide(quiet=True)
        model = "models/base_model.py"
        tests = "tests/test_models/test_base_model.py"
        results = psg.check_files([model, tests])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods(self):
        """
        Check Basemodel methods
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """
        Check object as instance of BaseModel
        """
        self.assertTrue(isinstance(self.bm, BaseModel))

    def test_str(self):
        """
        Check string representation of BaseModel object
        """
        bm_str = str(self.bm)
        self.assertEqual(True, "[BaseModel] ({})".format(self.bm.id) in bm_str)
        self.assertEqual(True, "created_at" in bm_str)
        self.assertEqual(True, "updated_at" in bm_str)
        self.assertEqual(True, "datetime.datetime" in bm_str)

    def test_save(self):
        """
        Check save method
        """
        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """
        Check dictionary method
        """
        bm_dict = self.bm.to_dict()
        self.assertEqual(self.bm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertEqual(type(bm_dict), dict)

    def tearDown(self):
        """
        Delete Base Model JSON file
        Checks file engine save method
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()
