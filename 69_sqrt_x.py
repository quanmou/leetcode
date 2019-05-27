class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        a = x/2 + 1
        b = (a + x/a) / 2
        while int(a) != int(b):
            a = b
            b = (a + x/a) / 2
        return int(a)

S = Solution()
print(S.mySqrt(1265628426))