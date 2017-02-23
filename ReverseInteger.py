class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        result = 0
        flag = x/abs(x)
        mid = abs(x) // 10
        suffix = abs(x) % 10
        while mid > 0:
            newresult = result * 10 + suffix
            if newresult // 10 != result:
                return 0
            result = newresult
            suffix = mid % 10
            mid //= 10

        newresult = result*10+suffix
        if newresult // 10 != result or newresult > 2**31:
            return 0
        return (newresult)*flag

