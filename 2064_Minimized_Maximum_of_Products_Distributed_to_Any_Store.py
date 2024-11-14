class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def canBeDistributed(amount):
            remaining_n = n
            for q in quantities:
                remaining_n -= math.ceil(q / amount)
                if remaining_n < 0:
                    return False
            return True

        left = 1
        right = max(quantities)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if canBeDistributed(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result
