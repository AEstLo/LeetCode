class Solution:
    def totalNQueens(self, n: int) -> int:

        def isValid(row: int, col: int) -> bool:
            for row2 in range(row):
                col2 = tab[row2]
                if col2 == col:
                    return False

                diff_cols = abs(col2 - col)
                diff_rows = row - row2  # always positive
                if diff_cols == diff_rows:
                    return False
            return True

        def solveNQueensBT(row: int):
            if row >= n:
                return 1
            total = 0
            for col in range(n):
                if isValid(row, col):
                    tab[row] = col
                    total += solveNQueensBT(row + 1)
            return total

        tab = [-1] * n
        return solveNQueensBT(0)
