class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        n = len(nums)
        ret = []
        i = 0
        while i < n and nums[i] < 0:
            num = nums[i]
            target = 0 - num
            
            l = i + 1
            r = n - 1
            while l < r:
                sum_nums = nums[l] + nums[r]
                if sum_nums == target:
                    num2 = nums[l]
                    num3 = nums[r]
                    ret.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == num2:
                        l += 1
                    while l < r and nums[r] == num3:
                        r -= 1
                elif sum_nums > target:
                    r -= 1
                else:
                    l += 1
            
            while i < n and num == nums[i]:
                i += 1
        if i < n - 2 and nums[i] == 0:
            if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 0:
                ret.append([0, 0, 0])
        return ret
        
