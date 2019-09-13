import unittest
import PythonGists.string as lib

class Test(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_explode_protected(self):
        """Tests the explode_protected function"""
        res1 = lib.explode_protected(",", "a, bcd, e, (f, g), h", ['()'])
        #self.assertIn(0, [0,1])
        self.assertEqual(res1, ["a", "bcd", "e", "(f, g)", "h"])

if __name__ == '__main__':
    unittest.main()