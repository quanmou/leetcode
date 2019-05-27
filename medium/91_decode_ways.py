class Solution:
    def numDecoding(self, s: str) -> int:
        length = len(s)
        if length == 0 or s[0] == '0':
            return 0

        dp = [0] * (length + 1)
        dp[0], dp[1] = 1, 1
        for i in range(1, length):
            if s[i] == '0':
                if int(s[i-1]) > 2 or s[i-1] == '0':
                    return 0
                dp[i+1] = dp[i-1]
            elif int(s[i-1:i+1]) > 26 or s[i-1] == '0':
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i] + dp[i-1]

        return dp[length]


S = Solution()
print(S.numDecoding("0"))  # 0
print(S.numDecoding("10"))  # 1
print(S.numDecoding("110"))  # 1
print(S.numDecoding("206"))  # 1
print(S.numDecoding("306"))  # 0
print(S.numDecoding("226"))  # 3
print(S.numDecoding("2260"))  # 0
