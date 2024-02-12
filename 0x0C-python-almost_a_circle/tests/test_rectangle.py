import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Set up some instances for testing
        self.r1 = Rectangle(10, 5, 2, 4, 1)
        self.r2 = Rectangle(5, 3, 0, 0, 2)

    def test_attributes(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 4)
        self.assertEqual(self.r1.id, 1)

        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 2)

    def test_area(self):
        self.assertEqual(self.r1.area(), 50)
        self.assertEqual(self.r2.area(), 15)

    def test_display(self):
        expected_output = "\n\n\n\n  ##########\n  ##########\n  ##########\n  ##########\n  ##########\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        self.r1.update(3, 7, 2, 1, 8)
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.width, 7)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 8)

        self.r2.update(id=4, width=6, height=3)
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r2.width, 6)
        self.assertEqual(self.r2.height, 3)

    def test_to_dictionary(self):
        expected_dict_r1 = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 4}
        self.assertEqual(self.r1.to_dictionary(), expected_dict_r1)

        expected_dict_r2 = {'id': 2, 'width': 5, 'height': 3, 'x': 0, 'y': 0}
        self.assertEqual(self.r2.to_dictionary(), expected_dict_r2)

if __name__ == '__main__':
    unittest.main()

