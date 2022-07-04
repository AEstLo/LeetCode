class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        total = m + n
        half = total // 2
        l = 0
        r = n - 1
        while True:
            mid = (l + r) // 2
            m_mid = half - mid - 2
            
            Nleft = nums2[mid] if mid >= 0 else float("-infinity")
            Nright = nums2[mid + 1]  if (mid + 1) < n else float("infinity")
            Mleft = nums1[m_mid] if m_mid >= 0 else float("-infinity")
            Mright = nums1[m_mid + 1]  if (m_mid + 1) < m else float("infinity")
            
            if Mleft <= Nright and Nleft <= Mright:
                if total % 2 != 0:
                    return min(Mright, Nright)
                else:
                    return (
                        min(Mright, Nright) + 
                        max(Mleft, Nleft)
                    ) / 2
            elif Nleft > Mright:
                r = mid - 1
            else:
                l = mid + 1

