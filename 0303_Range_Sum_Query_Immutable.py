class NumArray:

    def __init__(self, nums: List[int]):
        # Time: O(N)
        # Space: O(N)
        self.sumNums = [0] * len(nums)
        self.sumNums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sumNums[i] = nums[i] + self.sumNums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # Time: O(1)
        # Space: O(1)
        result = self.sumNums[right]
        if left > 0:
            result -= self.sumNums[left - 1]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Runtime: 114 ms, faster than 72.84% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.8 MB, less than 9.22% of Python3 online submissions for Range Sum Query - Immutable.
