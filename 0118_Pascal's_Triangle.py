class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time: O(N^2)
        # Space: O(N^2)
        result = [[1]]
        for i in range(2, numRows + 1):
            next_row = [1]
            for j in range(1, i - 1):
                next_row.append(result[i - 2][j] + result[i - 2][j - 1])
            next_row.append(1)
            result.append(next_row)
        return result

# Runtime: 45 ms, faster than 57.99% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 17.88% of Python3 online submissions for Pascal's Triangle.
