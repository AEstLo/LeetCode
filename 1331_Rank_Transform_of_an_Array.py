class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        # O(n log n)
        sorted_arr = sorted(arr)
        rank = 1
        map_elem_rank = {sorted_arr[0]: rank}
        n = len(arr)
        i = 1
        while i < n:
            if sorted_arr[i - 1] != sorted_arr[i]:
                rank += 1
                map_elem_rank[sorted_arr[i]] = rank
            i += 1
        return [map_elem_rank[elem] for elem in arr]
