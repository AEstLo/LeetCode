class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution = []
        S = len(s)

        def is_palindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(index, current_solution, current_str):
            if index >= S:
                if not current_str:
                    solution.append(list(current_solution))
                return

            # is palindrome?
            new_str = current_str + s[index]
            if is_palindrome(new_str):
                current_solution.append(new_str)
                backtracking(index + 1, current_solution, "")
                current_solution.pop()
            backtracking(index + 1, current_solution, new_str)

        backtracking(0, [], "")
        return solution
