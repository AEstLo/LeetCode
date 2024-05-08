class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = []
        for _ in range(numRows):
            lists.append([])
        i = 0
        while i < len(s):
            row = 0
            while i < len(s) and row < numRows:
                lists[row].append(s[i])
                row += 1
                i += 1
            row = numRows - 2
            while i < len(s) and row > 0:
                lists[row].append(s[i])
                row -= 1
                i += 1

        s_list = []
        for list_i in lists:
            s_list.append(''.join(list_i))
        return ''.join(s_list)
