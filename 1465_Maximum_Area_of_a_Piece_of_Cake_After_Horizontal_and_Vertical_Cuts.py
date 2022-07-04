class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def getMaxArea(arrCuts, boundary):
            if arrCuts:
                arrCuts.sort()

                prev = 0
                total = 0
                for cut in arrCuts:
                    currentCutSize = cut - prev
                    prev = cut
                    if total < currentCutSize:
                        total = currentCutSize
                # We have to compute the size till the end in the last cut
                currentCutSize = boundary - cut
                if total < currentCutSize:
                    total = currentCutSize
            else:
                total = boundary
            return total

        htotal = getMaxArea(horizontalCuts, h)
        vtotal = getMaxArea(verticalCuts, w)
        return vtotal * htotal % (10 ** 9 + 7)
