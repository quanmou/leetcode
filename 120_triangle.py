class Solution:
    def minimumTotal(self, triangle) -> int:
        min_sum = triangle.copy()
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j-1 >= 0:
                    pre_left = min_sum[i-1][j-1]
                else:
                    pre_left = float('inf')
                if j <= i-1:
                    pre_right = min_sum[i-1][j]
                else:
                    pre_right = float('inf')
                min_sum[i][j] = min(pre_left, pre_right) + triangle[i][j]
        return min(min_sum[-1])

S = Solution()
print(S.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
