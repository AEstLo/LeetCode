class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                result += 1
        return result
