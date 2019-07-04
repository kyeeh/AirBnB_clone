#!/usr/bin/python3
"""
Tests for Review Class
"""
import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test for Review Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Review Class
        """
        cls.rvw = Review()
        cls.rvw.place_id = "3773-pqrs"
        cls.rvw.user_id = "7337-abcd"
        cls.rvw.text = "Long happy customer review"

    @classmethod
    def teardown(cls):
        """
        Delete Review Class
        """
        del cls.rvw

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_methods(self):
        """
        Check Review and Basemodel methods
        """
        self.assertTrue(hasattr(Review, "__init__"))
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "to_dict"))

    def test_init(self):
        """
        Check object as instance of Review
        """
        self.assertTrue(isinstance(self.rvw, Review))

    def test_str(self):
        """
        Check string representation of Review object
        """
        rvw_str = str(self.rvw)
        self.assertEqual(True, "[Review] ({})".format(self.rvw.id) in rvw_str)
        self.assertEqual(True, "place_id" in rvw_str)
        self.assertEqual(True, "user_id" in rvw_str)
        self.assertEqual(True, "text" in rvw_str)

    def test_attr_types(self):
        """
        Check types defined
        """
        self.assertEqual(type(self.rvw.place_id), str)
        self.assertEqual(type(self.rvw.user_id), str)
        self.assertEqual(type(self.rvw.text), str)

    def test_save(self):
        """
        Check save method
        """
        self.rvw.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(self.rvw.created_at, self.rvw.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        rvw_dict = self.rvw.to_dict()
        self.assertEqual(self.rvw.__class__.__name__, 'Review')
        self.assertIsInstance(rvw_dict['created_at'], str)
        self.assertIsInstance(rvw_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
