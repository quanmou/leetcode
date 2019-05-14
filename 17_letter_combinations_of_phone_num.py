class Solution:
    def letterCombinations(self, digits: str) -> list:
        if len(digits) < 1:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for s in digits:
            res = [i + c for c in d[s] for i in res]
        return res

S = Solution()
print(S.letterCombinations('23'))
