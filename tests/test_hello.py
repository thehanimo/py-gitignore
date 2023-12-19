import unittest
import sys
import os

# Test from project directory in termial using: python -m unittest tests.test_hello
# Add the 'src' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from hello import say_hello


class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")

    def test_two_plus_two_equals_four(self):
        self.assertEqual(2 + 2, 4)
    
    def test_two_plus_two_equals_eight(self):
        self.assertNotEqual(2 + 2, 8)


if __name__ == "__main__":
    unittest.main()
