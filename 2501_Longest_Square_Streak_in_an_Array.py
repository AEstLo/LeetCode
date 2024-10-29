class Solution:
    def binarySearch(self, nums, low, high, target):
        if low > high:
            return False
        mid = low + ((high - low) // 2)
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            return self.binarySearch(nums, low, mid - 1, target)
        return self.binarySearch(nums, mid + 1, high, target)

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        max_subsequence = 0
        n = len(nums)
        visited = set()
        for num in nums:
            if num in visited:
                continue
            target = num * num
            if target > nums[-1]:
                continue
            subsequence = 1
            while self.binarySearch(nums, 0, n - 1, target):
                visited.add(target)
                subsequence += 1
                target *= target
            max_subsequence = max(subsequence, max_subsequence)
        return -1 if max_subsequence < 2 else max_subsequence
