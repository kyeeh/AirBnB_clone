#!/usr/bin/python3
"""
Tests for FileStorage Class
"""
import os
import pep8
import unittest
from models.__init__ import storage
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test for FileStorage Class
    """
    def setUp(self):
        """ set variables to be use """

    def tearDown(self):
        """ End the variables used """

    @classmethod
    def setUpClass(cls):
        """
        Set FileStorage Class
        """
        cls.fs = FileStorage()

    @classmethod
    def teardown(cls):
        """
        Delete FileStorage Class
        """
        del cls.fs
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """
        Check pep8
        """
        psg = pep8.StyleGuide(quiet=True)
        model = "models/engine/file_storage.py"
        tests = "tests/test_models/test_engine/test_file_storage.py"
        results = psg.check_files([model, tests])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_attributes(self):
        """
        Check FileStorage attributes
        """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(type(self.fs._FileStorage__objects) is dict)
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(type(self.fs._FileStorage__file_path) is str)

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
        self.assertIsNotNone(self.fs.all())
        self.assertTrue(type(self.fs.all()) is dict)

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

    def test_save(self):
        """
        Check save methods
        """
        storage = FileStorage()
        my_city = City()
        my_city.state_id = "37731-pqrs"
        my_city.name = "Caracas"
        my_city.save()
        self.assertTrue(os.path.isfile('file.json'))
        storage.reload()
        my_restored_city = storage.all()["City.{}".format(my_city.id)]
        self.assertTrue(my_restored_city.name == "Caracas")
        self.assertTrue(os.path.exists('file.json'))

    def test_restore(self):
        """
        Check restore methods
        """
        storage = FileStorage()
        my_city = City()
        my_city.state_id = "37731-pqrs"
        my_city.name = "Caracas"
        my_city.save()
        self.assertTrue(os.path.isfile('file.json'))
        storage.reload()
        my_restored_city = storage.all()["City.{}".format(my_city.id)]
        self.assertTrue(my_restored_city.name == "Caracas")
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(my_city.created_at,
                        my_city.updated_at)

    def test_objects_size(self):
        """
        Check replication for JSON and DICT
        """
        storage = FileStorage()
        size_prev = len(storage.all())
        my_city = City()
        my_city.state_id = "37731-pqrs"
        my_city.name = "Caracas"
        size_after = len(storage.all()) - 1
        self.assertTrue(size_prev == size_after)

if __name__ == "__main__":
    unittest.main()
