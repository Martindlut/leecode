class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        for num in nums:
            number ^= num
        return number
