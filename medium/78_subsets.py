class Solution(object):
    def gen(self, n):
        ret = []
        sub = [[0], [1]]
        if n == 0:
            return ret
        if n == 1:
            return sub
        for i in sub:
            for j in self.gen(n - 1):
                ret.append(i + j)
        return ret

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rts = []
        ls = self.gen(len(nums))

        for cur in ls:
            l = [nums[i] for i, e in enumerate(cur) if e == 1]
            rts.append(l)

        return rts

    def subsets(self, nums: list):
        res = []
        sub = [[], [nums[0]]]
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            return sub

        for e in sub:
            for num in self.subsets(nums[1:]):
                res.append(e + num)

        return res


S = Solution()
print(S.subsets([1,2,3]))