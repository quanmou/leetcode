class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # egg, add
        # foo, bar
        # ab, aa
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        if len(set(d.keys())) == len(set(d.values())):
            return True
        else:
            return False

s = Solution()
print(s.isIsomorphic('ab', 'aa'))