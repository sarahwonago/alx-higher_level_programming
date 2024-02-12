import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1, 'name': 'Alice'}]), '[{"id": 1, "name": "Alice"}]')

    def test_save_to_file(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Base.save_to_file([Base(1, 2)])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 2}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1, "name": "Alice"}]'), [{'id': 1, 'name': 'Alice'}])

    def test_create(self):
        obj = Base.create(id=1, name='Alice')
        self.assertEqual(obj.to_dictionary(), {'id': 1, 'name': 'Alice'})

    def test_load_from_file(self):
        Base.save_to_file([Base(1, 2)])
        objs = Base.load_from_file()
        self.assertEqual(objs[0].to_dictionary(), {'id': 1, 'width': 2})

if __name__ == "__main__":
    unittest.main()

