import main
import unittest

class TestSum(unittest.TestCase):
    def test_char(self):
        with self.assertRaises(TypeError):
            main.sum("a", "b")

if __name__ == '__main__':
    unittest.main()