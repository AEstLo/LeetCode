class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        def binary_search(arr, left, right, val):
            if left > right:
                left -= 1
                while left >= 0:
                    if arr[left][0] < val:
                        return left
                    left -= 1
                return -1
            mid = left + ((right - left) // 2)
            if arr[mid][0] == val:
                # look right until val is different:
                # We may have the same value with different beauties
                mid += 1
                while mid < len(arr) and arr[mid][0] == val:
                    mid += 1
                return mid - 1
            if arr[mid][0] < val:
                return binary_search(arr, mid + 1, right, val)
            return binary_search(arr, left, mid - 1, val)

        n = len(items)
        heap = list(items)
        heapq.heapify(heap)
        sorted_items = []
        while heap:
            sorted_items.append(heapq.heappop(heap))

        for i in range(1, n):
            sorted_items[i][1] = max(sorted_items[i-1][1], sorted_items[i][1])
        
        result = []
        for query in queries:
            pos = binary_search(sorted_items, 0, n - 1, query)
            if pos >= 0:
                value = sorted_items[pos][1]
            else:
                value = 0
            result.append(value)

        return result
