import unittest
import first

class TestFirst(unittest.TestCase):

    def test_add(self):

        result = first.add(3, 5)
        self.assertEqual(result, 7)



unittest.main()