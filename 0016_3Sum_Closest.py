class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = (2 * 10**4) + 1  # taken from description
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total == target:
                    return target
                if abs(total - target) < abs(diff):
                    diff = total - target
                if total < target:
                    l += 1
                else:
                    r -= 1
        return diff + target
