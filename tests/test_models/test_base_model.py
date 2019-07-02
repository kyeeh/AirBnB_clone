#!/usr/bin/python3
"""
Tests for BaseModel Class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test for BaseModel Class
    """

    @classmethod
    def setUpClass(self):
        """
        Set Base Model Class
        """
        self.bm = BaseModel()
        self.bm.name = "CLI"
        self.bm.num = 73

    @classmethod
    def teardown(self):
        """
        Delete Base Model Class
        """
        del self.bm

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

    def test_to_dict(self):
        """
        Check dictionary method
        """
        bm_dict = self.bm.to_dict()
        self.assertEqual(self.bm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
