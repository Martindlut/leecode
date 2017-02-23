class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = {}

        for i in range(0, len(nums)):
            if list.get(nums[i]) is None:
                list[target-nums[i]] = i
            else:
                return [list[nums[i]], i]