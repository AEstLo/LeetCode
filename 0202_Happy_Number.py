class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquares(x: int) -> int:
            """
            Given a number, replace it by the sum of the squares of its digits.
            Example: 19 -> 1 + 81 = 82
            O(K) being K the length of the number
            """
            result = 0
            while x > 0:
                result += (x % 10)**2
                x //= 10
            return result

        # Time complexity: O(N * K)
        # Space complexity: O(N)
        # being N the number of steps until we find 1 or a duplicate
        # being K the length of the longest number
        seen = set()

        while n != 1:
            seen.add(n)
            n = getSquares(n)
            if n in seen:
                return False
        return True
