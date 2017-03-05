class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nafter = 0
        nbefore = x
        while x >= 10:
            nafter = nafter * 10 + x % 10
            x //= 10
        nafter = nafter * 10 + x
        return nafter == nbefore