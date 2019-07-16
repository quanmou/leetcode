class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)

s = Solution()
print(s.containsDuplicate([1,2,3,1]))