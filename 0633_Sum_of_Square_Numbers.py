class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = {0}
        square = 0
        i = 0
        while square <= c:
            squares.add(square)
            i += 1
            square = i * i
        for square in squares:
            if (c - square) in squares:
                return True
        return False
