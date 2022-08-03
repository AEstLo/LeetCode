class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(index, new_target, current_candidate):
            if new_target < 0:
                return
            if new_target == 0:
                combinations.append(list(current_candidate))
                return

            i = index
            while i < len(candidates):
                if new_target - candidates[i] < 0:
                    break
                current_candidate.append(candidates[i])
                backtracking(i + 1, new_target -
                             candidates[i], current_candidate)
                current_candidate.pop()
                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1
            return

        backtracking(0, target, [])
        return combinations

# Runtime: 86 ms, faster than 74.87% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14 MB, less than 58.94% of Python3 online submissions for Combination Sum II.
