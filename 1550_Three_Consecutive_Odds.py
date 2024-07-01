class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        def isOddScore(num):
            return 1 if num % 2 != 0 else 0

        n = len(arr)
        if n < 3:
            return False
        i = 3
        consecutive = sum(isOddScore(arr[i]) for i in range(3))
        while i < n and consecutive < 3:
            consecutive -= isOddScore(arr[i - 3])
            consecutive += isOddScore(arr[i])
            i += 1
        return consecutive >= 3
