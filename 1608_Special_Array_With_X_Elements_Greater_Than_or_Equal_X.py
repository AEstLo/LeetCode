class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Sort O(nlogn)
        nums.sort()
        x = 1
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] < x:
                i += 1
            greater = len(nums) - i
            if x == greater:
                return x
            if x > greater:
                return -1
            x += 1

        return -1
        # Brute force O(n2)
        for x in range(1, len(nums) + 1):
            total = 0
            for num in nums:
                if num >= x:
                    total += 1
                    if total > x:
                        break
            if total == x:
                return x
        return -1
