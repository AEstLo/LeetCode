class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        nice_subarrays = 0
        r = 0
        odd_numbers = 0
        while r < n:
            while l < n and nums[l] % 2 == 0:
                l += 1
            if l >= n:
                return nice_subarrays
            if r <= l:
                odd_numbers += 1
                r = l + 1
            while r < n and odd_numbers < k:
                if nums[r] % 2 != 0:
                    odd_numbers += 1
                r += 1
            if odd_numbers < k:
                return nice_subarrays
            i = l - 1
            left_opt = 1
            while i >= 0 and nums[i] % 2 == 0:
                left_opt += 1
                i -= 1
            nice_subarrays += left_opt
            i = r
            while i < n and nums[i] % 2 == 0:
                nice_subarrays += left_opt
                i += 1
            l += 1
            odd_numbers -= 1
        return nice_subarrays
