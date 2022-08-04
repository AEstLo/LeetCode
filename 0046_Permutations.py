class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N*N!)
        # Space: O(N)
        result = []

        def backtracking(remaining_elements, permutation):
            if not remaining_elements:
                result.append(list(permutation))
            for num in remaining_elements:
                permutation.append(num)
                backtracking(remaining_elements - {num}, permutation)
                permutation.pop()
            return

        backtracking(set(nums), [])
        return result

# Runtime: 61 ms, faster than 55.39% of Python3 online submissions for Permutations.
# Memory Usage: 14.1 MB, less than 22.42% of Python3 online submissions for Permutations.
