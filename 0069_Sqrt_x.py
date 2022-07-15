class Solution:
    def mySqrtIterative(self, x: int) -> int:
        # Time: O(sqrt(x))
        # Space: O(1)
        sqrt = 1
        while sqrt * sqrt <= x:
            sqrt += 1
        return sqrt - 1

    def mySqrt(self, x: int) -> int:
        # Time: O(log(x))
        # Space: O(1)
        if x == 1:
            return 1
        left = 0
        right = x
        while left <= right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                left = middle + 1
            else:
                right = middle - 1
        return left - 1
