class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time: O(N*target)
        # Space: O(target)
        memo = {}

        def dfs(new_target):
            if new_target in memo:
                return memo[new_target]
            if new_target < 0:
                return 0
            if new_target == 0:
                return 1

            total = 0
            for num in nums:
                total += dfs(new_target - num)
            memo[new_target] = total
            return memo[new_target]

        total = dfs(target)
        return total

# Runtime: 41 ms, faster than 93.13% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.2 MB, less than 18.29% of Python3 online submissions for Combination Sum IV.
