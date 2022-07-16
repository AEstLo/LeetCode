class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)
        N = len(nums)
        pos = 0
        runner = 1
        while runner < N:
            if nums[runner] != nums[pos]:
                nums[pos + 1] = nums[runner]
                pos += 1
            runner += 1
        return pos + 1
