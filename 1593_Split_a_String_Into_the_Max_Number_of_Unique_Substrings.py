class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        solution = []
        result = [1]
        n = len(s)

        def isSolution(position):
            if position >= n:
                return True

            for i in range(position, n):
                substr = s[position:i+1]
                if substr in solution:
                    continue
                solution.append(substr)
                if isSolution(i + 1):
                    result[0] = max(result[0], len(solution))
                solution.pop()
            return False

        isSolution(0)
        return result[0]
