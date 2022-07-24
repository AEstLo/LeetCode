class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N^2)
        # Space: O(N)
        ret = []
        N = len(nums)
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, N - 1
            target = -nums[i]
            while l < r:
                val = nums[l] + nums[r]
                if val == target:
                    ret.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif val < target:
                    l += 1
                else:
                    r -= 1

        return ret

# Runtime: 716 ms, faster than 94.56% of Python3 online submissions for 3Sum.
# Memory Usage: 18.1 MB, less than 41.74% of Python3 online submissions for 3Sum.
