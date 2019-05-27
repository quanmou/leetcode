class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length < numRows or numRows == 1:
            return s
        ans = ''
        n = 2 * numRows - 2
        for i in range(numRows):
            for j in range(0, length - i, n):
                ans += s[j + i]
                if i != 0 and i != numRows - 1 and j + n - i < length:
                    ans += s[j + n - i]
        return ans


S = Solution()
print(S.convert("PAYPALISHIRING", numRows=3))  # "PAHNAPLSIIGYIR"
print(S.convert("PAYPALISHIRING", numRows=4))  # "PINALSIGYAHRPI"
print(S.convert("A", numRows=1))  # "A"
