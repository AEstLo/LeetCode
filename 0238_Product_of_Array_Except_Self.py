class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1)  - The output array does not count as extra space for space complexity analysis.
        product = [1] * len(nums)
        aux = 1
        for i in range(len(nums) - 1):
            aux *= nums[i]
            product[i+1] *= aux
        aux = 1
        for i in range(len(nums) - 1, 0, -1):
            aux *= nums[i]
            product[i - 1] *= aux
        return product

# Runtime: 389 ms, faster than 39.72% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.4 MB, less than 49.53% of Python3 online submissions for Product of Array Except Self.
