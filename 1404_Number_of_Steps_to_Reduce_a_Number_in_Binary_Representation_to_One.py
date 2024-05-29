class Solution:
    def numSteps(self, s: str) -> int:
        # In-place:
        # Runtime 33ms Beats 77.59% of users with Python3
        # Memory 16.42MB Beats 94.14% of users with Python3
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == "1":
                if not carry:
                    steps += 1
                carry = 1
            elif carry:
                steps += 1
            steps += 1

        if carry:
            steps += 1

        return steps

        # Converting to num
        number = 0
        for digit in s:
            number <<= 1
            if digit == '1':
                number |= 1

        steps = 0
        while number != 1:
            if number % 2 == 0:
                number >>= 1
            else:
                number += 1
            steps += 1
        return steps
