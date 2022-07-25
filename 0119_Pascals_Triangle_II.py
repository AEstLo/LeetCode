class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Time: O(N²)
        # Space: O(N)
        pascal = [1]*(rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                pascal[j] += pascal[j-1]
        return pascal

# Runtime: 34 ms, faster than 88.25% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.8 MB, less than 61.64% of Python3 online submissions for Pascal's Triangle II.
