class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Time: O(N)
        # Space: O(1)
        N = len(nums)
        found = False
        for i in range(1, N):
            if nums[i - 1] <= nums[i]:
                continue
            if found:
                return False
            found = True
            if i - 2 < 0 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
        return True

# Runtime: 199 ms, faster than 84.76% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.3 MB, less than 57.59% of Python3 online submissions for Non-decreasing Array.
