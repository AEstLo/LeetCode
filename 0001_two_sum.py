class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache_nums = {}
        len_nums = len(nums)
        for i in range(len_nums):
            num = nums[i]
            if num not in cache_nums:
                cache_nums[num] = [1, i, -1]
            elif cache_nums[num][2] == -1:  # From then on I do not care of repetitions
                cache_nums[num][0] += 1
                cache_nums[num][2] = i

        for i in range(len_nums):
            num = nums[i]
            diff = target - num
            if diff != num:
                if diff in cache_nums:
                    return [i, cache_nums[diff][1]]
            else:
                if diff in cache_nums and cache_nums[diff][2] != -1:
                    return [cache_nums[diff][1], cache_nums[diff][2]]
        return [-1, -1]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i
        return [-1, -1]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Runtime: 60 ms, faster than 97.37% of Python3 online submissions for Two Sum.
        # Memory Usage: 15.4 MB, less than 13.98% of Python3 online submissions for Two Sum.
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        return [-1, -1]
