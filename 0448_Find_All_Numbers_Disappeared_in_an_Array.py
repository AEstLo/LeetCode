class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1) -- because the result does not count in this problem, otherwise O(N)
        result = []
        for num in nums:
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

# Runtime: 715 ms, faster than 15.35% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 22.4 MB, less than 61.31% of Python3 online submissions for Find All Numbers Disappeared in an Array.
