class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            new_subsets = []
            for subset in ret:
                new_subset = list(subset)
                new_subset.append(num)
                new_subsets.append(new_subset)
            ret.extend(new_subsets)
        return ret
