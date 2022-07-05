class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        r = 0
        while r < 9:
            c = 0
            while c < 9:
                if board[r][c] != '.':
                    num = board[r][c]
                    if r not in rows:
                        rows[r] = set()
                    if num in rows[r]:
                        return False
                    rows[r].add(num)
                    if c not in cols:
                        cols[c] = set()
                    if num in cols[c]:
                        return False
                    cols[c].add(num)

                    box = (r // 3, c // 3)
                    if box not in boxes:
                        boxes[box] = set()
                    if num in boxes[box]:
                        return False
                    boxes[box].add(num)
                c += 1
            r += 1
        return True
