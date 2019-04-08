class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # method 1
        # start, end, begin, max_len = 0, 0, 0, 0
        # substring = {}
        # for i, c in enumerate(s):
        #     if c not in substring:
        #         substring[c] = i
        #     else:
        #         start = substring[c] + 1
        #         substring = {k: v for k, v in substring.items() if v >= start}
        #         substring[c] = i
        #
        #     end += 1
        #     if end - start > max_len:
        #         max_len = end - start
        #         begin = start
        #
        # print(s[begin:begin+max_len])
        # return max_len

        # method 2
        start, begin, max_len = 0, 0, 0
        substring = {}
        for i, c in enumerate(s):
            if c in substring:
                start = max(substring[c], start)

            # max_len = max(max_len, i - start + 1)
            if i - start + 1 > max_len:
                max_len = i - start + 1
                begin = start
            substring[c] = i + 1

        print(s[begin:begin + max_len])
        return max_len


S = Solution()
print(S.lengthOfLongestSubstring('abcabcbb'))  # 3, "abc"
print(S.lengthOfLongestSubstring('bbbbb'))     # 1, "b"
print(S.lengthOfLongestSubstring('pwwkew'))    # 3, "wke"
