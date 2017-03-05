class Solution(object):
    def titleToNumber(self, s):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        for char in s:
            number = number * 26 + (ord(char) - ord('A')) + 1
        return number
