class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        if i == -1 and j == -1:
            return '0'
        s, c = '', 0
        while i >= 0 and j >= 0:
            if a[i] == '0' and b[j] == '0':
                if c == 0:
                    s = '0' + s
                elif c == 1:
                    s = '1' + s
                    c = 0
            elif (a[i] == '0' and b[j] == '1') or (a[i] == '1' and b[j] == '0'):
                if c == 0:
                    s = '1' + s
                elif c == 1:
                    s = '0' + s
            elif a[i] == '1' and b[j] == '1':
                if c == 0:
                    s = '0' + s
                    c = 1
                elif c == 1:
                    s = '1' + s
            i -= 1
            j -= 1
        while i >= 0:
            if a[i] == '0':
                if c == 0:
                    s = '0' + s
                elif c == 1:
                    s = '1' + s
                    c = 0
            elif a[i] == '1':
                if c == 0:
                    s = '1' + s
                elif c == 1:
                    s = '0' + s
            i -= 1
        while j >= 0:
            if b[j] == '0':
                if c == 0:
                    s = '0' + s
                elif c == 1:
                    s = '1' + s
                    c = 0
            elif b[j] == '1':
                if c == 0:
                    s = '1' + s
                elif c == 1:
                    s = '0' + s
            j -= 1
        if c == 1:
            s = '1' + s
        return s

S = Solution()
print(S.addBinary('110010', '10111'))