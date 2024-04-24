import unittest
import os

class Tests(unittest.TestCase):
    def test_one(self):
        var1 = 1
        self.assertEqual(var1, 1, 'please set var1 to 1')

    def test_two(self):
        var2 = int(os.getenv('var2'))
        self.assertEqual(var2, 2, 'please set var2 to 2')
    
    def test_three(self):
        var3 = int(os.getenv('var3'))
        self.assertEqual(var3, 2, 'please set var3 to 3')
    
if __name__ == '__main__':
    unittest.main()