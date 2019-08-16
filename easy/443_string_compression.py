class Solution:
    def compress(self, chars) -> int:
        l = r = len(chars) - 1
        while l > 0:
            while l >= 0 and chars[l] == chars[r]:
                l -= 1
            if r - l > 1:
                chars[r] = str(r - l)
                for i in range(r - 2, l, -1):
                    del chars[i]
            r = l

        for i, ch in enumerate(chars):
            length = len(ch)
            if length > 1:
                del chars[i]
                for c in ch[::-1]:
                    chars.insert(i, c)


# l = ["a","b","b","c","c","c","a"]
l = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s = Solution()
s.compress(l)
print(l)

