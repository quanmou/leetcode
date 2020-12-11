class Solution:
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            tmp = {(), (num, )}
            for sub in subs:
                if sub and sub[-1] <= num:
                    tmp |= {sub + (num,)}
            subs |= tmp
        return [sub for sub in subs if len(sub) >= 2]


s = Solution()
print(s.findSubsequences([4,6,7,7]))
