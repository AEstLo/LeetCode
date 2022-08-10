class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            middle = left + (right - left) // 2
            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle
        return letters[left % len(letters)]

# Runtime: 115 ms, faster than 92.51% of Python3 online submissions for Find Smallest Letter Greater Than Target.
# Memory Usage: 14.4 MB, less than 20.86% of Python3 online submissions for Find Smallest Letter Greater Than Target.
