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
