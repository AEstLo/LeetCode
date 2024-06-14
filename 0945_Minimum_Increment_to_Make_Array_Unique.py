class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        increment = 0
        max_num = max(nums)
        counter = [0] * (max_num + 1 + len(nums))
        for num in nums:
            counter[num] += 1
        for i in range(len(counter)):
            if counter[i] > 1:
                counter[i + 1] += counter[i] - 1
                increment += counter[i] - 1
        return increment
