class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i = 0
        l1 = len(haystack)
        l2 = len(needle)
        while i <= l1 - l2:
            j = 0
            pos = i
            if haystack[i] == needle[j]:
                while i < l1 and j < l2 and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == l2:
                    return pos
            i = pos + 1

        return -1

S = Solution()
# print(S.strStr("hello", "ll"))
# print(S.strStr("aaaabba", "bba"))
print(S.strStr("mississippi", "issip"))
