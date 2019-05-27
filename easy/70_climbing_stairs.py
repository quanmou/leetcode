class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        a = 0
        b = 1
        for i in range(n):
            temp = a + b
            a = b
            b = temp
        return b


S = Solution()
print(S.climbStairs(3))  # 3
print(S.climbStairs(1))  # 1
