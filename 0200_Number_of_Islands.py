from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                r1, c1 = q.pop()
                if (r1, c1) in visited or not (0<=r1<m) or not (0<=c1<n) or grid[r1][c1] == "0":
                    continue
                q.appendleft((r1 - 1, c1))
                q.appendleft((r1 + 1, c1))
                q.appendleft((r1, c1 - 1))
                q.appendleft((r1, c1 + 1))
                visited.add((r1, c1))

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands


g1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
g2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(g1))
print(s.numIslands(g2))
