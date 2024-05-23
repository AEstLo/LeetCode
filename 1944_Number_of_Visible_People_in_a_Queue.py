class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        H = len(heights)
        result = [0] * H
        stack = []
        for i in range(H):
            while stack and heights[stack[-1]] < heights[i]:
                top_idx = stack.pop()
                result[top_idx] += 1
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        return result
