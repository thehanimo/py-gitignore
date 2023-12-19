import unittest
from src.hello import say_hello


class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")

    def test_two_plus_two_equals_four(self):
        self.assertEqual(2 + 2, 4)
    
    def test_say_hello_type(self):
        """Test that the return type of say_hello is str"""
        self.assertIsInstance(say_hello(), str)

    def test_say_hello_value(self):
        """Test that the return value of say_hello is 'Hello, World!'"""
        self.assertEqual(say_hello(), 'Hello, World!')

    def test_say_hello_not_empty(self):
        """Test that the return value of say_hello is not an empty string"""
        self.assertTrue(len(say_hello()) > 0)


if __name__ == "__main__":
    unittest.main()
