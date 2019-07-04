#!/usr/bin/python3
"""
Tests for FileStorage Class
"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set Base Model Class
        """
        cls.fs = FileStorage()
        cls.city = City()
        cls.city.state_id = "3773-pqrs"
        cls.city.name = "Bogotá"        
        try:
            os.remove("file.json")
        except Exception:
            pass        

    @classmethod
    def teardown(cls):
        """
        Delete Base Model Class
        """
        del cls.fs

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_methods(self):
        """
        Check FileStorage methods
        """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_init(self):
        """
        Check objects as instance of FileStorage
        """
        self.assertTrue(isinstance(self.fs, FileStorage))

    def test_all(self):
        """
        Check objects dictionary
        """      
        self.assertIsNotNone(self.fs.all)
        self.assertTrue(type(self.fs.all is dict))

    def test_new(self):
        """
        Check save method
        """
        storage = FileStorage()
        objects = storage.all()
        my_city = City()
        my_city.state_id = "37731-pqrs"
        my_city.name = "Caracas"
        storage.new(my_city)
        key = my_city.__class__.__name__ + "." + str(my_city.id)
        self.assertIsNotNone(objects[key])

    def test_save_and_restore(self):
        """
        Check save adn restore methods
        """
        storage = FileStorage()
        my_city = City()
        my_city.state_id = "37731-pqrs"
        my_city.name = "Caracas"
        my_city.save()
        storage.reload()
        my_restored_city = storage.all()["City.{}".format(my_city.id)]
        self.assertTrue(my_restored_city.name == "Caracas")

if __name__ == "__main__":
    unittest.main()
