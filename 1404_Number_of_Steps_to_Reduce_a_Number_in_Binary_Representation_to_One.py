class Solution:
    def numSteps(self, s: str) -> int:
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
