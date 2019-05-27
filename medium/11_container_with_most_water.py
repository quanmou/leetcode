class Solution:
    def maxArea(self, height: list) -> int:
        length = len(height)
        if length <= 1:
            return 0
        maxArea = 0

        # method 1 -> time limit exceeded
        # for i in range(length):
        #     for j in range(i+1, length):
        #         area = (j-i)*min(height[i], height[j])
        #         if area > maxArea:
        #             maxArea = area

        # method 2
        # left, right = 0, length - 1
        # maxArea = (right - left) * min(height[left], height[right])
        # while left < right:
        #     if height[right] >= height[left]:
        #         left += 1
        #     else:
        #         right -= 1
        #     if (right - left) * min(height[left], height[right]) > maxArea:
        #         maxArea = (right - left) * min(height[left], height[right])

        # method 3
        left, right, maxArea = 0, length - 1, 0
        maxNum = max(height)
        while left < right and maxNum * (right - left) > maxArea:
            maxArea = max(maxArea, (right - left)*min(height[left], height[right]))
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1

        return maxArea

S = Solution()
print(S.maxArea([1,8,6,2,5,4,8,3,7]))
print(S.maxArea([1]))
