class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        result = 0
        while num > 0:
            result *= 10
            result += num % 10
            num //= 10
        if x < 0:
            sign = -1
            result *= -1
            if result < -2**31:
                result = 0
        else:
            if result > 2**31 - 1:
                result = 0
        return result
