class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
             30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC',
             400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
        n1 = num // 1000
        n2 = (num - n1*1000) // 100
        n3 = (num - n1*1000 - n2*100) // 10
        n4 = num - n1*1000 - n2*100 - n3*10
        res = ''
        if n1 != 0:
            res += d[n1*1000]
        if n2 != 0:
            res += d[n2*100]
        if n3 != 0:
            res += d[n3*10]
        if n4 != 0:
            res += d[n4]
        return res
