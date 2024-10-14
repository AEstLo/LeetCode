class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxq = []
        for num in nums:
            heapq.heappush(maxq, -num)

        score = 0
        while k > 0:
            value = heapq.heappop(maxq)
            score -= value
            heapq.heappush(maxq, -1 * math.ceil(value/-3))
            k -= 1
        return score
