class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def isValidCoordinate(r, c):
            return 0<=r<n and 0<=c<n

        def getNeightbors(r, c):
            return (
                (r+1, c),
                (r-1, c),
                (r, c+1),
                (r, c-1),
            )

        n = len(grid)

        q = deque()
        inf = 2**31
        manhattan_distance = [[inf] * n for i in range(n)]
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    q.append((0, row, col))
                    manhattan_distance[row][col] = 0

        while q:
            dist, row, col = q.popleft()
            for neigh_row, neigh_col in getNeightbors(row, col):
                if (
                    isValidCoordinate(neigh_row, neigh_col) and
                    manhattan_distance[neigh_row][neigh_col] == inf
                ):
                    manhattan_distance[neigh_row][neigh_col] = 1 + dist
                    q.append((1 + dist, neigh_row, neigh_col))

        heap = [(-manhattan_distance[0][0], 0, 0)]
        visited = {(0, 0)}
        while heap:
            neg_dist, row, col = heapq.heappop(heap)

            if row == n - 1 and col == n - 1:
                return -neg_dist
            for neigh_row, neigh_col in getNeightbors(row, col):
                if (
                    isValidCoordinate(neigh_row, neigh_col) and
                    (neigh_row, neigh_col) not in visited
                ):
                    visited.add((neigh_row, neigh_col))
                    dist = min(
                        manhattan_distance[neigh_row][neigh_col],
                        -neg_dist,
                    )
                    heapq.heappush(heap, (-dist, neigh_row, neigh_col))
        return 0
