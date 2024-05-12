class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # brute force

        def getMaxValue(r, c):
            max_value = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if grid[i][j] > max_value:
                        max_value = grid[i][j]
            return max_value

        n = len(grid)
        if n < 2:
            return []
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for row in range(1, n - 1):
            for col in range(1, n - 1):
                result[row - 1][col - 1] = getMaxValue(row, col)
        return result
