class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = len(nums)
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         j = i
        #         while j < l-1 and nums[j] == 0:
        #             j += 1
        #         temp = nums[j]
        #         nums[j] = nums[i]
        #         nums[i] = temp

        # method 2
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[zero] == 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        print(nums)

S = Solution()
S.moveZeroes([0,1,0,3,12])
S.moveZeroes([0,1,0])
S.moveZeroes([0,0,1])
