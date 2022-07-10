from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time: O(m + n)
        # Space: O(1)
        nums1_i = m - 1
        nums2_i = n - 1
        i = n + m - 1
        while nums1_i >= 0 and nums2_i >= 0:
            if nums1[nums1_i] >= nums2[nums2_i]:
                nums1[i] = nums1[nums1_i]
                nums1_i -= 1
            else:
                nums1[i] = nums2[nums2_i]
                nums2_i -= 1
            i -= 1
        while nums2_i >= 0:
            nums1[i] = nums2[nums2_i]
            nums2_i -= 1
            i -= 1
        return
