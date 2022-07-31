class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)

        # Let's use a monothonic stack
        stack = []

        result = [-1] * len(nums)

        # test: 1,2,1
        # i = 0
        #   stack = 0
        #   result = -1,-1,-1
        # i = 1
        #   stack = 1
        #   result = 1,-1,-1
        # i = 2
        #   stack = 1,2
        #   result = 1,-1,-1
        for i in range(2*len(nums)):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                index = stack.pop()
                result[index] = nums[i % len(nums)]
            if i < len(nums):
                stack.append(i)

        return result

# Runtime: 237 ms, faster than 87.83% of Python3 online submissions for Next Greater Element II.
# Memory Usage: 15.5 MB, less than 96.98% of Python3 online submissions for Next Greater Element II.
