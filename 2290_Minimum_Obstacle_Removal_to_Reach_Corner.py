class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_heap = [(0, 0, 0)]
        path = set()

        while min_heap:
            obstacles, row, col = heapq.heappop(min_heap)
            if not (0<=row<m) or not (0<=col<n) or (row, col) in path:
                continue
            if row == m - 1 and col == n - 1:
                return obstacles + grid[row][col]
            path.add((row, col))
            heapq.heappush(min_heap, (obstacles + grid[row][col], row + 1, col))
            heapq.heappush(min_heap, (obstacles + grid[row][col], row - 1, col))
            heapq.heappush(min_heap, (obstacles + grid[row][col], row, col + 1))
            heapq.heappush(min_heap, (obstacles + grid[row][col], row, col - 1))
            
        return -1
