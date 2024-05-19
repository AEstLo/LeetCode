class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_heap = []
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total == target:
                    return target
                heapq.heappush(min_heap, (abs(total - target), total - target))
                if total < target:
                    l += 1
                else:
                    r -= 1
        _, diff = heapq.heappop(min_heap)
        return diff + target
