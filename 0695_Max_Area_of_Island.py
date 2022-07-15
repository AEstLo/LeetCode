from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time: O(M * N)
        Space: O(M * N)
        """
        M = len(grid)
        N = len(grid[0])
        seen = set()

        def getMaxAreaOfIsland(row, col):
            k = (row, col)
            if not (0 <= row < M) or not (0 <= col < N) or grid[row][col] == 0 or k in seen:
                return 0

            seen.add(k)
            return 1 + getMaxAreaOfIsland(row - 1, col) + \
                getMaxAreaOfIsland(row + 1, col) + \
                getMaxAreaOfIsland(row, col - 1) + \
                getMaxAreaOfIsland(row, col + 1)

        current_max = 0
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 1:
                    current_max = max(
                        current_max, getMaxAreaOfIsland(row, col))
        return current_max


s = Solution()
gr = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(s.maxAreaOfIsland(gr))
