class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        N = len(s)
        while i < N and s[i] == ' ':
            i += 1
        if i >= N:
            return 0

        if s[i] == '-':
            negative = -1
            i += 1
        elif s[i] == '+':
            negative = 1
            i += 1
        else:
            negative = 1

        while i < N and s[i] == '0':
            i += 1

        if i >= N or not ('0' < s[i] <= '9'):
            return 0

        stack = []
        while i < N and '0' <= s[i] <= '9':
            stack.append(ord(s[i]) - ord('0'))
            i += 1

        if not stack:
            return 0

        total = 0
        i = 1
        max_val = 2**31
        while stack:
            num = stack.pop()
            total += i * num
            if total >= max_val:
                total = negative * max_val
                if negative > 0:
                    total -= 1
                return total
            i *= 10
        if total >= max_val:
            total = max_val
            if negative > 0:
                total -= 1
        return negative * total
