class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            fathest = 0
            for i in range(l, r + 1):
                fathest = max(fathest, i + nums[i])
            l = r + 1
            r = fathest
            jumps += 1
        
        return jumps
