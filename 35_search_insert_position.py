class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target and nums[mid - 1] != target:
                    return mid
                else:
                    r = mid - 1
        return l

S = Solution()
print(S.searchInsert([1,3], 2))
print(S.searchInsert([1,3,5,6], 7))
print(S.searchInsert([1], 2))
