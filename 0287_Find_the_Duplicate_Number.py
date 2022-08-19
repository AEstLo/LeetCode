class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Runtime: 626 ms, faster than 98.17% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 27.9 MB, less than 56.16% of Python3 online submissions for Find the Duplicate Number.
