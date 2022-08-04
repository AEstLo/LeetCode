class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(num, path):
            if len(path) == k:
                result.append(list(path))
                return
            if num > n:
                return
            for i in range(num, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()
        backtracking(1, [])
        return result

# Runtime: 663 ms, faster than 40.90% of Python3 online submissions for Combinations.
# Memory Usage: 16 MB, less than 52.65% of Python3 online submissions for Combinations.
