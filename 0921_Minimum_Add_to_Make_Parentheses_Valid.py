class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        moves = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    moves += 1
        return left + moves
