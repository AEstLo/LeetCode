class Solution:

    def getColValues(self, board, col):
        s = set([board[row][col]
                for row in range(9) if board[row][col] != '.'])
        return s

    def getBoxValues(self, board, row, col):
        rbox = 3 * (row // 3)
        cbox = 3 * (col // 3)
        s = set()
        for r in range(rbox, rbox + 3):
            for c in range(cbox, cbox + 3):
                if board[r][c] != '.':
                    s.add(board[r][c])
        return s

    def solveSudoku(self, board: List[List[str]]) -> None:
        possible_values_set = set([str(i) for i in range(1, 10)])
        self.solveSudokuBT(board, possible_values_set)

    def solveSudokuBT(self, board: List[List[str]], possible_values_set: set) -> None:
        for row in range(9):
            rowValues = set(board[row])
            rowValues.discard('.')
            for col in range(9):
                if board[row][col] == '.':
                    possibleVals = possible_values_set - rowValues - \
                        self.getColValues(board, col) - \
                        self.getBoxValues(board, row, col)
                    if not possibleVals:
                        return False

                    for val in possibleVals:
                        board[row][col] = val
                        is_valid = self.solveSudokuBT(
                            board, possible_values_set)
                        if is_valid:
                            return True
                        board[row][col] = '.'
                    return False  # nothing is valid
        return True
