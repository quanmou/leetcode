class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return '1'
        s = '1'
        d = {'1': '11', '11': '21', '111': '31', '2': '12', '22': '22', '222': '32', '3': '13', '33': '23', '333': '33'}
        for i in range(0, n - 1):
            temp = new_s = ''
            for j in range(len(s)):
                if temp == '' or s[j] == temp[-1]:
                    temp += s[j]
                else:
                    new_s += d[temp]
                    temp = s[j]
                if j == len(s) - 1:
                    new_s += d[temp]

            s = new_s
        return s

S = Solution()
print(S.countAndSay(6))
