class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def getOnes(num: int) -> int:
            ones = 0
            while num > 0:
                if num & 1:
                    ones += 1
                num >>= 1
            return ones
        
        i = 1
        cache_ones = {}
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if nums[i] not in cache_ones:
                    cache_ones[nums[i]] = getOnes(nums[i])
                if nums[i-1] not in cache_ones:
                    cache_ones[nums[i-1]] = getOnes(nums[i-1])
                if cache_ones[nums[i]] != cache_ones[nums[i-1]]:
                    return False
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i = 0
            i += 1
        return True
