class Solution:
    def permute(self, nums: list) -> list:
        # nums.sort()
        # res = []
        # def gen(n):
        #     out = [[]]
        #     i = 0
        #     while i < n:
        #         temp = []
        #         for o in out:
        #             for j in range(len(o) + 1):
        #                 t = o.copy()
        #                 t.insert(j, i)
        #                 temp.append(t)
        #         out = temp
        #         yield out
        #         i += 1
        # for o in gen(len(nums)):
        #     pass
        # for idx in o:
        #     res.append([nums[i] for i in idx])
        # return res

        # method 2
        from functools import reduce
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p) + 1)], nums, [[]])


S = Solution()
print(S.permute([1,3,5]))