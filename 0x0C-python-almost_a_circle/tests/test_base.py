import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """Set up for each test."""
        Base._Base__nb_objects = 0 

    def test_constructor(self):
        """Test the constructor of Base."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_to_json_string(self):
        """Test the to_json_string method."""
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")
        self.assertEqual(b.to_json_string([]), "[]")

        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = b.to_json_string(data)
        self.assertEqual(json_str, json.dumps(data))

    def test_save_to_file(self):
        """Test the save_to_file method."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        filename = "Base.json"
        Base.save_to_file([b1, b2, b3])

        with open(filename, 'r') as file:
            content = file.read()
            expected_content = '[{"id": 1}, {"id": 2}, {"id": 3}]'
            self.assertEqual(content, expected_content)

    def test_from_json_string(self):
        """Test the from_json_string method."""
        b = Base()
        json_str = '[]'
        self.assertEqual(b.from_json_string(json_str), [])

        data = [{"id": 1}, {"id": 2}, {"id": 3}]
        json_str = json.dumps(data)
        self.assertEqual(b.from_json_string(json_str), data)

    def test_create(self):
        """Test the create method."""
        r = Base.create(id=5, width=10, height=20)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_load_from_file(self):
        """Test the load_from_file method."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        filename = "Base.json"
        Base.save_to_file([b1, b2, b3])

        loaded_instances = Base.load_from_file()
        self.assertEqual(len(loaded_instances), 3)
        self.assertEqual(loaded_instances[0].id, b1.id)
        self.assertEqual(loaded_instances[1].id, b2.id)
        self.assertEqual(loaded_instances[2].id, b3.id)

if __name__ == '__main__':
    unittest.main()

