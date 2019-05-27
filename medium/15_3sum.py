class Solution:
    def threeSum(self, nums: list) -> list:
        res = []

        # method 1 -> time limit exceeded
        # neg_nums = {i: -1*n for i, n in enumerate(nums)}
        # keys = list(neg_nums.keys())
        # values = list(neg_nums.values())
        #
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum in neg_nums.values():
        #             idx = keys[values.index(sum)]
        #             if idx != i and idx != j:
        #                 res.append(tuple(sorted([nums[i], nums[j], nums[idx]])))
        # res = list(set(res))

        # method 2
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res

S = Solution()
print(S.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
