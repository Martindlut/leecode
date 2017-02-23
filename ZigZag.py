class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        list = []
        for i in range(0, numRows):
            list.append([])

        for index in range(0, len(s)):
            i = index % (2*(numRows - 1))
            if i//numRows == 0:
                list[i % numRows].append(s[index])
            else:
                list[numRows-i-2].append(s[index])
        return ''.join([''.join(item) for item in list])