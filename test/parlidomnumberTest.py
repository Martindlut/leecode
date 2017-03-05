import unittest
import parlidomnumber


class MyTestCase(unittest.TestCase):

    def test_zigzag(self):
        solution = parlidomnumber.Solution()
        result = solution.isPalindrome(121)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
