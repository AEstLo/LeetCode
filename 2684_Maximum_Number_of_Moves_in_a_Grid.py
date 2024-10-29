class Solution:
    def getTotal(self, grid, row, column, prev_value, memo):
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] <= prev_value:
            return 0
        if memo[row][column] < 0:
            memo[row][column] = 1 + max(
                self.getTotal(grid, row - 1, column + 1, grid[row][column], memo),
                self.getTotal(grid, row, column + 1, grid[row][column], memo),
                self.getTotal(grid, row + 1, column + 1, grid[row][column], memo),
            )
        return memo[row][column]

    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_moves = 0
        memo = []
        for row in range(m):
            memo.append([-1 for _ in range(len(grid[row]))])
        for row in range(m):
            max_moves = max(max_moves, self.getTotal(grid, row, 0, -1, memo))
        return max_moves - 1
