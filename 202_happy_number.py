class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        d = {}
        while n != 1:
            s, y = n // 10, n % 10
            temp = 0
            while s != 0:
                temp += y ** 2
                s, y = s // 10, s % 10
            temp += y**2

            if n not in d:
                d[n] = temp
                n = temp
            else:
                return False
        return True

S = Solution()
print(S.isHappy(19))
