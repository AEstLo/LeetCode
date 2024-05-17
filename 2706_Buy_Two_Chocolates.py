class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices_heap = []
        for price in prices:
            heapq.heappush(prices_heap, price)
        
        total = heapq.heappop(prices_heap)
        total += heapq.heappop(prices_heap)
        if total <= money:
            return money - total
        return money
