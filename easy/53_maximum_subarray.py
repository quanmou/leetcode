class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


S = Solution()
print(S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6, [4, -1, 2, 1]
