#!/usr/bin/python3
"""
Tests for City Class
"""
import os
import pep8
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test for City Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup City Class
        """
        cls.city = City()
        cls.city.state_id = "3773-pqrs"
        cls.city.name = "Bogotá"

    @classmethod
    def teardown(cls):
        """
        Delete City Class
        """
        del cls.city
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_City(self):
        """
        Check pep8
        """
        psg = pep8.StyleGuide(quiet=True)
        model = "models/city.py"
        tests = "tests/test_models/test_city.py"
        results = psg.check_files([model, tests])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_attributes(self):
        """
        Check User attributes
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_methods(self):
        """
        Check City and Basemodel methods
        """
        self.assertTrue(hasattr(City, "__init__"))
        self.assertTrue(hasattr(City, "__str__"))
        self.assertTrue(hasattr(City, "save"))
        self.assertTrue(hasattr(City, "to_dict"))

    def test_init(self):
        """
        Check object as instance of City
        """
        self.assertTrue(isinstance(self.city, City))

    def test_str(self):
        """
        Check string representation of City object
        """
        city_str = str(self.city)
        self.assertEqual(True, "[City] ({})".format(self.city.id) in city_str)
        self.assertEqual(True, "name" in city_str)
        self.assertEqual(True, "state_id" in city_str)
        self.assertEqual(True, "created_at" in city_str)
        self.assertEqual(True, "updated_at" in city_str)
        self.assertEqual(True, "datetime.datetime" in city_str)

    def test_save(self):
        """
        Check save method
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """
        Check dictionary method
        """
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertEqual(type(city_dict), dict)

if __name__ == "__main__":
    unittest.main()
