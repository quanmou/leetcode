class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        # method 1
        # c = 0
        # for i in range(len(nums)):
        #     if nums[i-c] == val:
        #         nums.pop(i-c)
        #         c += 1
        # return len(nums)

        # method 2
        # s = f = 0
        # while f < len(nums):
        #     if nums[f] != val:
        #         nums[s] = nums[f]
        #         s += 1
        #     f += 1
        # return s

        # method 3
        while val in nums:
            nums.remove(val)
        return len(nums)

S = Solution()
# print(S.removeElement([3,3], 3))  # [2, 2]
# print(S.removeElement([3,2,2,3], 3))  # [2, 2]
print(S.removeElement([0,1,2,2,3,0,4,2], 2))  # [0,1,3,0,4]
