class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def getUniquePathsIII(row, col):
            if row < 0 or row >= M or col < 0 or col >= N or grid[row][col] < 0:
                return 0
            if grid[row][col] == 2:
                for i in range(M):
                    for j in range(N):
                        if grid[i][j] == 0:
                            return 0
                return 1
            grid[row][col] = -1
            total = getUniquePathsIII(row + 1, col)
            total += getUniquePathsIII(row - 1, col)
            total += getUniquePathsIII(row, col + 1)
            total += getUniquePathsIII(row, col - 1)
            grid[row][col] = 0
            return total

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return getUniquePathsIII(r, c)
        return 0
