import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        """Create a Square instance for testing."""
        self.square = Square(5, 2, 3, 1)

    def test_size(self):
        """Test the size property and setter."""
        self.assertEqual(self.square.size, 5)
        self.square.size = 10
        self.assertEqual(self.square.size, 10)

    def test_update(self):
        """Test the update method."""
        self.square.update(10, 20, 30, 40)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 30)
        self.assertEqual(self.square.y, 40)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        square_dict = self.square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_str(self):
        """Test the __str__ method."""
        square_str = str(self.square)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(square_str, expected_str)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

