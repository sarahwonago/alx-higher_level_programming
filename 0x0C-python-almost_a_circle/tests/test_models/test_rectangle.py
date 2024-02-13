import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rect_creation(self):
        rect_1 = Rectangle(1, 2)
        self.assertIsNotNone(rect_1.id)

        rect_2 = Rectangle(1, 2, 3)
        self.assertIsNotNone(rect_2.id)

        rect_3 = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(rect_3.id)

        with self.assertRaises((TypeError, ValueError)):
            Rectangle("1", 2)

        with self.assertRaises((TypeError, ValueError)):
            Rectangle(1, "2")

        with self.assertRaises((TypeError, ValueError)):
            Rectangle(1, 2, "3")

        with self.assertRaises((TypeError, ValueError)):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_str(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(rect), "[Rectangle] (6) 4/5 - 2/3")

    def test_display(self):
        rect = Rectangle(2, 3, 1, 1)
        expected_output = "\n ##\n ##\n ##\n"
        with self.assertLogs() as log:
            rect.display()
        self.assertEqual(log.output, expected_output)

    def test_to_dictionary(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        expected_dict = {'id': 6, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_update(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.update(7, 8, 9, 10, 11)
        self.assertEqual(str(rect), "[Rectangle] (7) 10/11 - 8/9")

    def test_create(self):
        rect_dict = {'id': 12, 'width': 4, 'height': 5, 'x': 6, 'y': 7}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(str(rect), "[Rectangle] (12) 6/7 - 4/5")

    def test_save_load_file(self):
        rects = [Rectangle(2, 3, 4, 5, 6), Rectangle(3, 4, 5, 6, 7)]
        file_name = "rectangles.json"
        
        Rectangle.save_to_file(rects, file_name)

        loaded_rects = Rectangle.load_from_file(file_name)

        for orig_rect, loaded_rect in zip(rects, loaded_rects):
            self.assertEqual(str(orig_rect), str(loaded_rect))

if __name__ == '__main__':
    unittest.main()

