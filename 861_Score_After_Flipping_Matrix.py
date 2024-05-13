class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # We want to have all 0s in the first row because is the highest number
        M = len(grid)
        N = len(grid[0])
        for row in range(M):
            if grid[row][0] == 0:
                self.flipRow(row, grid)
        for col in range(1, N):
            total_ones = 0
            for row in range(M):
                total_ones += grid[row][col]
            if total_ones < M / 2:
                self.flipCol(col, grid)
        return self.getScore(grid)

    def getScore(self, grid: List[List[int]]) -> int:
        score = 0
        for row in range(len(grid)):
            for i in range(len(grid[row])):
                score += grid[row][-1 - i] * 2**i
        return score
    
    def flipRow(self, row, grid):
        for col in range(len(grid[row])):
            grid[row][col] = int(not(grid[row][col]))
    
    def flipCol(self, col, grid):
        for row in range(len(grid)):
            grid[row][col] = int(not(grid[row][col]))
