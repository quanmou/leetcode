class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = 0
        for c, num in enumerate(nums2):
            while nums1[pos] < num and pos < m + c:
                pos += 1
            nums1.insert(pos, num)
            pos += 1
            nums1.pop()


S = Solution()
n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
S.merge(n1, 3, n2, 3)
print(n1)