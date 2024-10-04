class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # O(n*k) in time
        # O(n+k) in space
        # ... Time limit exceeded
        # circles = defaultdict(int)
        # max_value = 0
        # for num in nums:
        #     for i in range(num - k, num + k + 1):
        #         circles[i] += 1
        #         if circles[i] > max_value:
        #             max_value = circles[i]
        # return max_value

        # Time: O(nlogn)
        # Space: O(1)
        nums.sort()
        n = len(nums)
        l = 0
        max_value = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            if max_value < r - l + 1:
                max_value = r - l + 1
        return max_value
