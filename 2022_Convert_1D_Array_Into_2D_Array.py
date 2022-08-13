class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Time: O(m * n)
        # Space: O(m * n)
        if len(original) != m * n:
            return []
        result = []
        row = 0
        i = 0
        while row < m:
            result.append(original[i:i+n])
            i += n
            row += 1
        return result

# Runtime: 1014 ms, faster than 96.42 % of Python3 online submissions for Convert 1D Array Into 2D Array.
# Memory Usage: 21.2 MB, less than 93.80 % of Python3 online submissions for Convert 1D Array Into 2D Array.
