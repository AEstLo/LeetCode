from typing import List


class Solution_1:
    def fourSum_1(self, nums: List[int], target: int) -> List[List[int]]:
        # Time: O(N^3)  (N^(k-1))
        # Space: O(N^2)
        N = len(nums)
        nums.sort()  # O(NlogN)
        res = []
        quad = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, N - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # base case
            l, r = start, N - 1
            while l < r:
                diff = nums[r] + nums[l]
                if diff < target:
                    l += 1
                elif diff > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res

# Runtime: 981 ms, faster than 63.04% of Python3 online submissions for 4Sum.
# Memory Usage: 13.9 MB, less than 93.83% of Python3 online submissions for 4Sum.


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # O(NlogN)
        current_sol = []
        res = self.kSum(4, nums, target, current_sol, 0)
        return res

    def kSum(self, k: int, nums: List[int], target: int, current_sol: List[int], start) -> List[List[int]]:
        ret = []
        if k == 2:
            two_sum = self.twoSum(nums, target, start=start)
            for ts in two_sum:
                ret.append(current_sol + ts)
            return ret
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current_sol.append(nums[i])
            k_sum = self.kSum(k - 1, nums, target -
                              nums[i], current_sol, i + 1)
            if k_sum:
                ret.extend(k_sum)
            current_sol.pop()
        return ret

    def twoSum(self, nums: List[int], target: int, start) -> List[List[int]]:
        ret = []
        l = start
        r = len(nums) - 1
        while l < r:
            sum_lr = nums[r] + nums[l]
            if sum_lr < target:
                l += 1
            elif sum_lr > target:
                r -= 1
            else:
                ret.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
        return ret

# Runtime: 1027 ms, faster than 61.00% of Python3 online submissions for 4Sum.
# Memory Usage: 13.9 MB, less than 64.73% of Python3 online submissions for 4Sum.
