class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        tab = [-1] * n
        results = []
        self.solveNQueensBT(n, 0, tab, results)
        return results
    
    def solveNQueensBT(self, n: int, row: int, tab: List[int], results: List[List[str]]):
        if row >= n:
            result_str = []
            for col in tab:
                join_str = ['.'] * n
                join_str[col] = 'Q'
                result_str.append(''.join(join_str))
            results.append(result_str)
            return
        for col in range(n):
            if self.isValid(n, row, col, tab):
                tab[row] = col
                self.solveNQueensBT(n, row + 1, tab, results)
        return
    
    def isValid(self, n: int, row: int, col: int, tab: List[int]) -> bool:
        for row2 in range(row):
            col2 = tab[row2]
            if col2 == col:
                return False
        
            diff_cols = abs(col2 - col)
            diff_rows = row - row2  # always positive
            if diff_cols == diff_rows:
                return False
        return True

