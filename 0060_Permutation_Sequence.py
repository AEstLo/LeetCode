class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Time: O(n^2)
        # Space: O(n)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        result = []
        unused = [i for i in range(1, n + 1)]
        k -= 1
        while n > 0:
            part_length = fact[n] // n
            i = k // part_length
            result.append(str(unused[i]))
            unused.pop(i)
            k %= part_length
            n -= 1
        return ''.join(result)
