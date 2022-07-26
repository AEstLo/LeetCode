class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        types = set()
        for candy in candyType:
            types.add(candy)
        return min(len(types), len(candyType) // 2)

# Runtime: 1540 ms, faster than 14.76% of Python3 online submissions for Distribute Candies.
# Memory Usage: 16.2 MB, less than 38.63% of Python3 online submissions for Distribute Candies.
