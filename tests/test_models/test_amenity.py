#!/usr/bin/python3
"""
Tests for Amenity Class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test for Amenity Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Amenity Class
        """
        cls.amnt = Amenity()
        cls.amnt.name = "Cundinamarca"

    @classmethod
    def teardown(cls):
        """
        Delete Amenity Class
        """
        del cls.amnt

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_methods(self):
        """
        Check Amenity and Basemodel methods
        """
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(hasattr(Amenity, "save"))
        self.assertTrue(hasattr(Amenity, "to_dict"))

    def test_init(self):
        """
        Check object as instance of Amenity
        """
        self.assertTrue(isinstance(self.amnt, Amenity))

    def test_str(self):
        """
        Check string representation of Amenity object
        """
        ste_str = str(self.amnt)
        self.assertEqual(True, "[Amenity] ({})".format(self.amnt.id) in ste_str)
        self.assertEqual(True, "name" in ste_str)
        self.assertEqual(True, "created_at" in ste_str)
        self.assertEqual(True, "updated_at" in ste_str)
        self.assertEqual(True, "datetime.datetime" in ste_str)

    def test_save(self):
        """
        Check save method
        """
        self.amnt.save()
        self.assertNotEqual(self.amnt.created_at, self.amnt.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        amnt_dict = self.amnt.to_dict()
        self.assertEqual(self.amnt.__class__.__name__, 'Amenity')
        self.assertIsInstance(amnt_dict['created_at'], str)
        self.assertIsInstance(amnt_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
