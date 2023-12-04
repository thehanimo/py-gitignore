import unittest
from src.hello import say_hello


class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")

    def test_two_plus_two_equals_four(self):
        self.assertEqual(2 + 2, 4)


if __name__ == "__main__":
    unittest.main()
