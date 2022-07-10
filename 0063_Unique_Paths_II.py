class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time: O(M * N)
        # Space: O(M * N)
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        memo = {}

        def getUniquePathsWithObstacles(row, col):
            if row >= M or col >= N or obstacleGrid[row][col]:
                return 0
            if row == M - 1 and col == N - 1:
                return 1
            k = f'{row},{col}'
            if k in memo:
                return memo[k]
            memo[k] = getUniquePathsWithObstacles(
                row + 1, col) + getUniquePathsWithObstacles(row, col + 1)
            return memo[k]
        return getUniquePathsWithObstacles(0, 0)
