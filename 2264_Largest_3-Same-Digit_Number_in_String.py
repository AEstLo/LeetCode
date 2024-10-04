class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_numbers = [False for __ in range(10)]
        acum = 0
        prev = ''
        for c in num:
            if prev == c:
                acum += 1
                if acum >= 3:
                    good_numbers[int(c)] = True
            else:
                acum = 1
                prev = c

        for i in range(9, -1, -1):
            if good_numbers[i]:
                return str(i) * 3
        return ""
