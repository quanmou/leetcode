class Solution:
    def generateParenthesis(self, n: int) -> list:
        # wrong answer, when n==4, no '(())(())'
        # res = []
        # if n < 1:
        #     return []
        # if n == 1:
        #     return ['()']
        # temp = self.generateParenthesis(n-1)
        # res.extend(['(' + p + ')' for p in temp])
        # res.extend(['()' + p for p in temp])
        # res.extend([p + '()' for p in temp])
        # return list(set(res))

        #
        res = {'(': [1, 0]}
        for i in range(1, 2*n):
            temp = {}
            for p in res:
                if res[p][0] < n:
                    temp[p + '('] = [res[p][0]+1, res[p][1]]
                if res[p][1] < n and res[p][1] < res[p][0]:
                    temp[p + ')'] = [res[p][0], res[p][1]+1]
            res = temp.copy()
        return list(res.keys())

S = Solution()
print(S.generateParenthesis(1))
