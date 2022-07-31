class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(N1 + N2)
        # Space: O(N1 + N2)
        # Let's use a monothonic stack
        stack = []
        greaters = [-1] * len(nums2)
        lookup = {num: i for i, num in enumerate(nums2)}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                greaters[index] = nums2[i]
            stack.append(i)

        ans = [-1] * len(nums1)

        for i, num in enumerate(nums1):
            ans[i] = greaters[lookup[num]]
        return ans

# Runtime: 56 ms, faster than 87.25% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.1 MB, less than 56.94% of Python3 online submissions for Next Greater Element I.
