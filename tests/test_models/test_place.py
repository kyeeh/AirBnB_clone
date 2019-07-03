#!/usr/bin/python3
"""
Tests for Place Class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test for Place Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Place Class
        """
        cls.place = Place()
        cls.place.name = "Cundinamarca"

    @classmethod
    def teardown(cls):
        """
        Delete Place Class
        """
        del cls.place

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_methods(self):
        """
        Check Place and Basemodel methods
        """
        self.assertTrue(hasattr(Place, "__init__"))
        self.assertTrue(hasattr(Place, "__str__"))
        self.assertTrue(hasattr(Place, "save"))
        self.assertTrue(hasattr(Place, "to_dict"))

    def test_init(self):
        """
        Check object as instance of Place
        """
        self.assertTrue(isinstance(self.place, Place))

    def test_str(self):
        """
        Check string representation of Place object
        """
        plc_str = str(self.place)
        self.assertEqual(True, "[Place] ({})".format(self.place.id) in plc_str)
        self.assertEqual(True, "city_id" in plc_str)
        self.assertEqual(True, "user_id" in plc_str)
        self.assertEqual(True, "name" in plc_str)
        self.assertEqual(True, "description" in plc_str)
        self.assertEqual(True, "number_rooms" in plc_str)
        self.assertEqual(True, "number_bathrooms" in plc_str)
        self.assertEqual(True, "max_guest" in plc_str)
        self.assertEqual(True, "price_by_night" in plc_str)
        self.assertEqual(True, "number_bathrooms" in plc_str)
        self.assertEqual(True, "latitude" in plc_str)
        self.assertEqual(True, "longitude" in plc_str)
        self.assertEqual(True, "amenity_ids" in plc_str)
        self.assertEqual(True, "created_at" in plc_str)
        self.assertEqual(True, "updated_at" in plc_str)
        self.assertEqual(True, "datetime.datetime" in plc_str)

    def test_save(self):
        """
        Check save method
        """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """
        Check dictionary method
        """
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.__class__.__name__, 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
