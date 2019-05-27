class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        length = len(nums)
        if length < 4:
            return []

        res = []
        nums.sort()
        i = 0
        while i < length -3:
            j = i+1
            while j < length - 2:
                l, r = j+1, length-1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
                j += 1
                while nums[j] == nums[j-1] and j < length - 2:
                    j += 1
            i += 1
            while nums[i] == nums[i-1] and i < length - 3:
                i += 1
        return res

S = Solution()
# print(S.fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# print(S.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))  # [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(S.fourSum([-1, -5, -5, -3, 2, 5, 0, 4], -7))  # [[-5,-5,-1,4],[-5,-3,-1,2]]
