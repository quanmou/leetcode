class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) <= 1:
            return len(nums)

        # standard method
        # s, f = 0, 1
        # while f < len(nums):
        #     if nums[f] != nums[s]:
        #         s += 1
        #         nums[s] = nums[f]
        #     f += 1
        # return s + 1

        # my slow method
        c = 0
        for i in range(1, len(nums)):
            if nums[i-c] in nums[:i-c]:
                nums.remove(nums[i-c])
                c += 1
        return len(nums)

S = Solution()
# n = [1, 1, 2]
# n = [0,0,1,1,1,2,2,3,3,4]
# n = [1, 2, 3]
n = [1, 1]
k = S.removeDuplicates(n)
print(n[:k])
