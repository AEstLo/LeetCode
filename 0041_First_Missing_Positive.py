class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 10
        for i in range(n):
            num = abs(nums[i])
            if 0 <= num - 1 < n and nums[num - 1] > 0:
                nums[num - 1] *= -1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
