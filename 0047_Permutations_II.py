class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N*N!)
        # Space: O(N)
        result = []
        N = len(nums)
        c_nums = collections.Counter(nums)
        permutation = []

        def backtracking():
            if len(permutation) == N:
                result.append(list(permutation))
                return
            for num in c_nums:
                if c_nums[num] <= 0:
                    continue
                permutation.append(num)
                c_nums[num] -= 1
                backtracking()
                c_nums[num] += 1
                permutation.pop()
            return

        backtracking()
        return result

# Runtime: 130 ms, faster than 31.14% of Python3 online submissions for Permutations II.
# Memory Usage: 14.4 MB, less than 23.48% of Python3 online submissions for Permutations II.
