class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(index, current_target, current_combination):
            if current_target < 0:
                return
            if current_target == 0:
                combinations.append(list(current_combination))
                return
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                if current_target - candidate < 0:
                    current_combination.pop()
                    break
                backtracking(i, current_target - candidate,
                             current_combination)
                current_combination.pop()
            return

        backtracking(0, target, [])
        return combinations

# Runtime: 73 ms, faster than 94.50% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.3 MB, less than 12.12% of Python3 online submissions for Combination Sum.
