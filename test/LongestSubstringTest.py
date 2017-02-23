import unittest
import LongestSubstring


class MyTestCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        test = LongestSubstring.Solution()
        result = test.lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(result, 3)
        result = test.lengthOfLongestSubstring('bbbbb')
        self.assertEqual(result, 1)
        result = test.lengthOfLongestSubstring('pwwkew')
        self.assertEqual(result, 3)

