class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if len(s) == 0 or s[0] not in '-+0123456789':
            return 0
        sign = 1
        if s[0] in '-+':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        if len(s) == 0:
            return 0
        num = 0
        for i, c in enumerate(s):
            if c in '0123456789':
                num = num*10 + int(c)
            else:
                break
        res = sign*num
        if res < -1 * 2**31:
            res = -1 * 2**31
        if res > 2**31 - 1:
            res = 2**31 - 1
        return res


S = Solution()
print(S.myAtoi("2147483648"))

