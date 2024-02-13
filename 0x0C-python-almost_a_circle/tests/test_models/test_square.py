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

        # Add more tests for different scenarios...

    def test_invalid_square_creation(self):
        # Test Square("1")
        with self.assertRaises(ValueError):
            Square("1")

        # Test Square(1, "2")
        with self.assertRaises(ValueError):
            Square(1, "2")

        # Test Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(1, 2, "3")

        # Add more tests for different scenarios...

    def test_str_method(self):
        # Test __str__() for Square
        square = Square(3, 4, 5)
        self.assertEqual(str(square), "[Square] (0) 4/5 - 3")

    def test_to_dictionary_method(self):
        # Test to_dictionary() for Square
        square = Square(3, 4, 5, 1)
        square_dict = {'id': 1, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), square_dict)

    def test_update_method(self):
        # Test update() for Square
        square = Square(3, 4, 5, 1)
        square.update(2, 6, 7, 8)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 2)

    def test_create_method(self):
        # Test create() for Square
        square_dict = {'id': 1, 'size': 3, 'x': 4, 'y': 5}
        square = Square.create(**square_dict)
        self.assertEqual(square.to_dictionary(), square_dict)

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

