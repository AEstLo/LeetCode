class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def maxJumpsRecursive(idx, memo):
            if memo[idx] > 0:
                return memo[idx]
            if (idx >= len(arr) - 1 or arr[idx] <= arr[idx + 1]) and (idx == 0 or arr[idx] <= arr[idx - 1]):
                memo[idx] = 1
                return 1

            maxV = 0
            for i in range(idx-d, idx):
                if i >= 0 and i < len(arr):
                    if arr[i] < arr[idx]:
                        maxJumpsRecursive(i, memo)
                        if maxV < memo[i]:
                            maxV = memo[i]
                    else:
                        maxV = 0
            maxV2 = 0
            for i in range(idx + 1, idx + d + 1):
                if i >= 0 and i < len(arr):
                    if arr[i] < arr[idx]:
                        maxJumpsRecursive(i, memo)
                        if maxV2 < memo[i]:
                            maxV2 = memo[i]
                    else:
                        break
            memo[idx] = 1 + max(maxV, maxV2)
            return memo[idx]
        memo = [0] * len(arr)
        for j in range(len(arr)):
            maxJumpsRecursive(j, memo)
        return max(memo)
