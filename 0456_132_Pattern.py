class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Time: O(N)
        # Space: O(N)
        stack_greater = []
        greater = [-1] * len(nums)

        minimum = [0] * len(nums)
        minimum[0] = nums[0]
        for i in range(1, len(nums)):
            minimum[i] = min(minimum[i - 1], nums[i])

        for i in range(len(nums) - 1, -1, -1):
            # greater
            while stack_greater and nums[stack_greater[-1]] < nums[i]:
                index = stack_greater.pop()
                greater[index] = i
            stack_greater.append(i)

        for i in range(len(nums) - 1, -1, -1):
            if greater[i] >= 0 and minimum[greater[i]] < nums[i]:
                return True
        return False

# Runtime: 683 ms, faster than 22.22% of Python3 online submissions for 132 Pattern.
# Memory Usage: 32.2 MB, less than 40.42% of Python3 online submissions for 132 Pattern.
