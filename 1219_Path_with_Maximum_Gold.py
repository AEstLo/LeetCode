class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = 0
        path = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_gold_cell = self.getMaximumGoldRecursion(grid, row, col, path)
                if max_gold_cell > result:
                    result = max_gold_cell
        return result
    
    def getMaximumGoldRecursion(self, grid, row, col, path):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        tup = (row, col)
        if tup in path:
            return 0
        path.add(tup)
        result = grid[row][col] + max(
            self.getMaximumGoldRecursion(grid, row, col + 1, path),
            self.getMaximumGoldRecursion(grid, row, col - 1, path),
            self.getMaximumGoldRecursion(grid, row + 1, col, path),
            self.getMaximumGoldRecursion(grid, row - 1, col, path),
        )
        path.discard(tup)
        return result
