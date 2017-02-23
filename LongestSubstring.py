class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = {}
        longest = 0
        for index in range(len(s)):
            if flag.get(s[index]) is None:
                flag[s[index]] = index
            else:
                if longest < len(flag):
                    longest = len(flag)
                oldpos = flag.get(s[index])
                for key, value in flag.items():
                    if value < oldpos:
                        del flag[key]
                flag[s[index]] = index
        if longest < len(flag):
            longest = len(flag)
        return longest
