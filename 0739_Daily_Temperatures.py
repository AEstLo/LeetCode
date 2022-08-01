class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        # Let's use a monothonic stack
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

# Runtime: 1744 ms, faster than 56.72% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 24.7 MB, less than 70.66% of Python3 online submissions for Daily Temperatures.
