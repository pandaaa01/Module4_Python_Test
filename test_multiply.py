import unittest

def multiply(x, y):
    return x*y

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(4, 7), 30)

if __name__ == '__main__':
    unittest.main()