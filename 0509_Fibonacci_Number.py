class Solution:
    def fib(self, n: int) -> int:
        # Fibonacci using three variables
        # Time: O(n)
        # Space: O(1)
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        c = a + b
        i = 3
        while i <= n:
            a = b
            b = c
            c = a + b
            i += 1
        return c
