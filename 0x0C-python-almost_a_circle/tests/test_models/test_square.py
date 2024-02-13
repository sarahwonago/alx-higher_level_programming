import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        # Test Square(1)
        square_1 = Square(1)
        self.assertEqual(square_1.size, 1)

        # Test Square(1, 2)
        square_2 = Square(1, 2)
        self.assertEqual(square_2.size, 1)
        self.assertEqual(square_2.x, 2)

        # Test Square(1, 2, 3)
        square_3 = Square(1, 2, 3)
        self.assertEqual(square_3.size, 1)
        self.assertEqual(square_3.x, 2)
        self.assertEqual(square_3.y, 3)

    def test_invalid_square_creation(self):
        # Test Square("1")
        with self.assertRaises(ValueError):
            Square("1")

    def test_str_method(self):
        # Test __str__() for Square
        square = Square(3, 4, 5)
        self.assertEqual(str(square), "[Square] (0) 4/5 - 3")

    def test_save_and_load_from_file_methods(self):
        # Test save_to_file() and load_from_file() for Square
        filename = "test_square.json"
        square = Square(3, 4, 5, 1)

        # Save to file
        Square.save_to_file([square], filename)

        # Load from file
        loaded_squares = Square.load_from_file(filename)
        self.assertEqual(len(loaded_squares), 1)
        self.assertEqual(loaded_squares[0].to_dictionary(), square.to_dictionary())

if __name__ == '__main__':
    unittest.main()
