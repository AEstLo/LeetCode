from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Time: O (N log N)
        # Space: O(N)
        import heapq
        N = len(nums)
        INF = float('-infinity')
        memo = [None] * N
        memo[N - 1] = nums[N - 1]
        heap = [(nums[N - 1] * -1, N - 1 - k)]
        for i in range(N - 2, -1, -1):
            while i < heap[0][1]:
                heapq.heappop(heap)
            memo[i] = heap[0][0] * -1 + nums[i]
            heapq.heappush(heap, (memo[i] * -1, i - k))
        return memo[0]
