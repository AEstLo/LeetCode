class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largestArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                s, h = stack.pop()
                start = s
                area = (i - s) * h
                if area > largestArea:
                    largestArea = area
            stack.append((start, height))

        n = len(heights)
        for s, h in stack:
            area = (n - s) * h
            if area > largestArea:
                largestArea = area
        return largestArea
