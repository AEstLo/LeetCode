class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Iterative
        # Runtime: 361 ms, faster than 54.19% of Python3 online submissions for Binary Search.
        # Memory Usage: 15.4 MB, less than 72.77% of Python3 online submissions for Binary Search.
        # Time: O(logN)
        # Space: O(1)
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def searchRecursive(self, nums: List[int], target: int) -> int:
        # Recursive
        # Runtime: 465 ms, faster than 18.50% of Python3 online submissions for Binary Search.
        # Memory Usage: 23 MB, less than 22.84% of Python3 online submissions for Binary Search.
        # Time: O(logN)
        # Space: O(logN)
        def bs(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(mid + 1, r)
            else:
                return bs(l, mid - 1)
        return bs(0, len(nums) - 1)
