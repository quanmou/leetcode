class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        m = [[0]*(l2+1) for i in range(l1+1)]
        for i in range(1, l1+1):
            m[i][0] = i
        for j in range(1, l2+1):
            m[0][j] = j
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    m[i][j] = m[i-1][j-1]
                else:
                    m[i][j] = min(m[i-1][j-1], m[i-1][j], m[i][j-1]) + 1
        return m[-1][-1]



s = Solution()
print(s.minDistance('horse', 'ros'))
