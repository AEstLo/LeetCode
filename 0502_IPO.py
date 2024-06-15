class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        capitals = [(capital[i], profits[i]) for i in range(n)]
        capitals.sort()
        heap_profits = []
        maximized_capital = w
        i = 0
        while k > 0:
            while i < n and capitals[i][0] <= maximized_capital:
                heappush(heap_profits, -capitals[i][1])
                i += 1
            if not heap_profits:
                break
            maximized_capital -= heappop(heap_profits)
            k -= 1
        return maximized_capital
