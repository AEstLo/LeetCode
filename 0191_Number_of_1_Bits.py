class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 1
        total = 0
        for __ in range(33):
            if i & n != 0:
                total += 1
            i <<= 1
        return total

