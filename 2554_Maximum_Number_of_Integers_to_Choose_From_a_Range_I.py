class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        output = 0
        i = 1
        while maxSum >= i and i <= n:
            if i not in banned_set:
                maxSum -= i
                output += 1
            i += 1
        return output
