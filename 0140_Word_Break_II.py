class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)  # to find words in O(1)
        solution = []
        S = len(s)

        def backtracking(start, end, current_solution):
            if end > S:
                if S == start:
                    solution.append(" ".join(current_solution))
                return
            backtracking(start, end + 1, current_solution)
            substr = s[start:end]
            if substr in wordSet:
                current_solution.append(substr)
                backtracking(end, end + 1, current_solution)
                current_solution.pop()
        
        backtracking(0, 1, [])
        return solution
