class Solution:
    def countSmaller1(self, nums: List[int]) -> List[int]:
        # Time: O(N^2)
        # Space: O(N)
        N = len(nums)
        ret = [0] * N
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    ret[i] += 1
        return ret

    def countSmaller(self, nums):
        # Time: O(N log N)
        # Space: O(N)
        N = len(nums)
        res = [0] * N
        res_idx = 0
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res[res_idx] = getSum(rank[x] - 1)
            res_idx += 1
            update(rank[x])
        return res[::-1]

# Runtime: 3031 ms, faster than 80.90% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 33.5 MB, less than 66.81% of Python3 online submissions for Count of Smaller Numbers After Self.
