def mergesort(a):
    def merge(result, helper_a, l, r, mid):
        i = l
        while i <= r:
            helper_a[i] = result[i]
            i+=1

        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if helper_a[i] <= helper_a[j]:
                result[k] = helper_a[i]
                i += 1
            else:
                result[k] = helper_a[j]
                j += 1
            k += 1
        while i <= mid:
            result[k] = helper_a[i]
            i += 1
            k += 1

    def divide(result, helper_a, l, r):
        if l < r:
            mid = l + (r - l) // 2
            divide(result, helper_a, l, mid)
            divide(result, helper_a, mid + 1, r)
            merge(result, helper_a, l, r, mid)

    result = list(a)
    helper_a = [0] * len(a)
    divide(result, helper_a, 0, len(a) - 1)
    return result

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = mergesort(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                result += 1
        return result
