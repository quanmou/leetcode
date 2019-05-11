class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows+1):
            temp = [1]
            pre = res[i-1]
            for j in range(1, i-1):
                temp.append(pre[j-1] + pre[j])
            temp.append(1)
            res.append(temp)
        res.remove([1, 1])
        return res

S = Solution()
print(S.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
