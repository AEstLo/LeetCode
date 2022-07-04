class Solution:
    def romanToInt(self, s: str) -> int:
        romanConversionDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        i = len(s) - 1
        total = 0
        while i >= 0:
            total += romanConversionDict[s[i]]
            if s[i] in ('V', 'X'):
                if i - 1 >= 0 and s[i - 1] == 'I':
                    total -= romanConversionDict[s[i - 1]]
                    i -= 1
            elif s[i] in ('L', 'C'):
                if i - 1 >= 0 and s[i - 1] == 'X':
                    total -= romanConversionDict[s[i - 1]]
                    i -= 1
            elif s[i] in ('D', 'M'):
                if i - 1 >= 0 and s[i - 1] == 'C':
                    total -= romanConversionDict[s[i - 1]]
                    i -= 1
            i -= 1
        return total
