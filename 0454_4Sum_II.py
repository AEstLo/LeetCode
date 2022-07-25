from typing import List
import collections


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Time: O(N²)
        # Space: O(N²)
        c = 0
        d = collections.defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                d[num1 + num2] += 1

        for num1 in nums3:
            for num2 in nums4:
                c += d[-num1-num2]

        return c

# Runtime: 902 ms, faster than 62.64% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.1 MB, less than 71.82% of Python3 online submissions for 4Sum II.
