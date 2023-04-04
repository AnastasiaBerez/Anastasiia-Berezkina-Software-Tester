import unittest
from triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle()

    def test_perimeter(self):
        self.assertEqual(self.triangle.perimeter(5, 4, 3), 12)

    def test_area(self):
        self.assertEqual(self.triangle.area(5, 4, 3), 6)

    def test_is_valid(self):
        self.assertEqual(self.triangle.is_valid(5, 4, 3), True)

if __name__ == "__main__":
        unittest.main()