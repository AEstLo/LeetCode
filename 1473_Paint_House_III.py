from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], H: int, C: int, T: int) -> int:
        # THIS IS NOT MY SOLUTION: Credits to Larry: https://www.youtube.com/watch?v=2J4tkJ7v3r4
        cache = [[[None for _ in range(T + 1)]
                  for _ in range(C + 1)] for _ in range(H + 1)]
        has_cache = [
            [[False for _ in range(T + 1)] for _ in range(C + 1)] for _ in range(H + 1)]
        INF = 1000001

        def getMinCost(index, last_color, neighborhoods):
            # Time: O(H * C^2 * T)
            # Space: O(H * C * T)
            if index == H:
                if neighborhoods == T:
                    return 0
                return INF
            if neighborhoods > T:
                return INF

            if has_cache[index][last_color][neighborhoods]:
                return cache[index][last_color][neighborhoods]

            has_cache[index][last_color][neighborhoods] = True

            if houses[index] == 0:
                ans = INF

                for current_color in range(1, C + 1):
                    if current_color == last_color:
                        ans = min(ans, getMinCost(index + 1, current_color,
                                  neighborhoods) + cost[index][current_color - 1])
                    else:
                        ans = min(ans, getMinCost(
                            index + 1, current_color, neighborhoods + 1) + cost[index][current_color - 1])
            else:
                current_color = houses[index]
                if current_color == last_color:
                    ans = getMinCost(index + 1, current_color, neighborhoods)
                else:
                    ans = getMinCost(index + 1, current_color,
                                     neighborhoods + 1)

            cache[index][last_color][neighborhoods] = ans
            return ans

        minimum_cost = getMinCost(0, 0, 0)
        if minimum_cost >= INF:
            minimum_cost = -1
        return minimum_cost
