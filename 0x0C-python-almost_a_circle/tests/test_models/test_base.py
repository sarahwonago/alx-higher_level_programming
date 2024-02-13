import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_custom_id_assignment(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_dict_list(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_string_with_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_with_dict_string(self):
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()

