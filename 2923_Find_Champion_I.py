class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for col in range(n):
            for row in range(n):
                if grid[row][col]:
                    break
            else:
                return col
        return -1
