class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)

        result = [0] * len(nums)
        l = 0
        i = r = len(nums) - 1
        while i >= 0:
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] * nums[l]
                l += 1
            else:
                result[i] = nums[r] * nums[r]
                r -= 1
            i -= 1
        return result

# Runtime: 318 ms, faster than 64.46% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.2 MB, less than 49.11% of Python3 online submissions for Squares of a Sorted Array.
