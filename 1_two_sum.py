class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        # method1
        # new_nums = [target - n for n in nums]  # [7, 2, -2, -6]
        # for i, m in enumerate(new_nums):
        #     for j, n in enumerate(nums):
        #         if m == n and i != j:
        #             return [i, j]

        # method2
        # d = {n: i for i, n in enumerate(nums)}
        # for i, m in enumerate(nums):
        #     if target - m in d and i != d[target-m]:
        #         return [i, d[target-m]]

        # method3
        d = {}
        for i, m in enumerate(nums):
            if m in d:
                return [d[m], i]
            else:
                d[target - m] = i


S = Solution()
print(S.twoSum([2, 7, 11, 15], 9))
print(S.twoSum([3, 2, 4], 6))
