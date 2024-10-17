class Solution:
    def maximumSwap(self, num: int) -> int:
        numstr = str(num)
        highestnumstr = sorted(str(num), reverse=True)
        n = len(numstr)
        for i in range(n):
            if numstr[i] != highestnumstr[i]:
                for j in range(n-1, i, -1):
                    if numstr[j] == highestnumstr[i]:
                        return int(numstr[:i] + numstr[j] + numstr[i + 1:j] + numstr[i] + numstr[j+1:])
                raise Exception("should not reach this point")
        return num
