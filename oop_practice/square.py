import unittest

def square(num):
    return num*num


class TestSquare(unittest.TestCase):

    def test_square_positive(self):
        result = square(4)
        self.assertEqual(result, 16)

    def test_square_negative(self):
        result = square(-4)
        self.assertEqual(result, 16)

    def test_invalid_input(self):
        # Check how the function behaves with invalid input
        with self.assertRaises(TypeError):
            square("a")

if __name__ == "__main__":
  unittest.main()