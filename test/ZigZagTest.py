import unittest
import ZigZag


class MyTestCase(unittest.TestCase):

    def test_zigzag(self):
        a = ZigZag.Solution()
        list = 'ABCDE'
        result = a.convert(list, 4)
        self.assertEqual(result == 'ABCED')


if __name__ == '__main__':
    unittest.main()
