class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = []
        for num in nums:
            heapq.heappush(delta, num - (num^k))
        total = sum(nums)
        while delta:
            delta_1 = heapq.heappop(delta)
            if delta:
                delta_2 = heapq.heappop(delta)
                sum_deltas = -delta_1 - delta_2
                if sum_deltas > 0:
                    total += sum_deltas
        return total
