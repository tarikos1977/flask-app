import unittest
from app import hello_world

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello, World!')
    
    def test_hello_world_uppercase(self):
        self.assertEqual(hello_world().upper(), 'HELLO, WORLD!')

if __name__ == '__main__':
    unittest.main()
