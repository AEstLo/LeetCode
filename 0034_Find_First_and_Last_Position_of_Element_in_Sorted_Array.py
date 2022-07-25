from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        res = [-1, -1]

        def binarySearch(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == N - 1 or nums[mid + 1] != nums[mid]:
                    res[1] = mid
                else:
                    binarySearch(mid + 1, end)
                if mid == 0 or nums[mid - 1] != nums[mid]:
                    res[0] = mid
                else:
                    binarySearch(start, mid - 1)
            elif nums[mid] < target:
                binarySearch(mid + 1, end)
            else:
                binarySearch(start, mid - 1)

        binarySearch(0, N - 1)
        return res

# Runtime: 162 ms, faster than 20.92% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 93.21% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
