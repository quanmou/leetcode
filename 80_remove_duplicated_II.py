class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # method 1
        # if len(nums) < 3:
        #     return len(nums)
        # pos = 1
        # for i in range(1, len(nums)-1):
        #     if nums[i-1] != nums[i+1]:
        #         nums[pos] = nums[i]
        #         pos += 1
        # nums[pos] = nums[-1]
        # return pos + 1

        # method 2
        n = len(nums)
        if n < 2:
            return n
        s = f = 2
        while f < n:
            if nums[s - 2] != nums[f]:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s

