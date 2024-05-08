class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def merge_sort(start, end, l: List[int]) -> List[int]:
            if start > end:
                return []
            if start == end:
                return [l[start]]
            mid = (end + start) // 2
            left = merge_sort(start, mid, l)
            right = merge_sort(mid + 1, end, l)
            return merge(left, right)

        def merge(left, right):
            result = []
            for i in left:
                result.append(i)
            for i in right:
                result.append(i)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result[k] = left[i]
                    i += 1
                else:
                    result[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                result[k] = left[i]
                i += 1
                k += 1
            return result

        sorted_scores = merge_sort(0, len(score) - 1, score)
        cache_positions = {}

        medals = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        i = len(score) - 1
        while i >= 0 and medals:
            medal = medals.pop()
            cache_positions[sorted_scores[i]] = medal
            i -= 1

        pos = 4
        while i >= 0:
            cache_positions[sorted_scores[i]] = str(pos)
            pos += 1
            i -= 1

        result = []
        for s in score:
            result.append(cache_positions[s])
        return result
