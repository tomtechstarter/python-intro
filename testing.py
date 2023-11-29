# Funktion: addiere
def addiere(x, y):
    return x + y

# Unittest
import unittest

class TestAddition(unittest.TestCase):

    def test_addition_positiv(self):
        self.assertEqual(addiere(2, 3), 5)

    def test_addition_negativ(self):
        self.assertEqual(addiere(-2, 3), 1)

    def test_addition_mit_null(self):
        self.assertEqual(addiere(0, 0), 0)

if __name__ == '__main__':
    unittest.main()