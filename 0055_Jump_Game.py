class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        target = N - 1
        for i in range(N - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
