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
                return mid
            if arr[mid][0] < val:
                return binary_search(arr, mid + 1, right, val)
            return binary_search(arr, left, mid - 1, val)

        heap = list(items)
        heapq.heapify(heap)
        sorted_items = []
        prev_price = heap[0][0]
        max_beauty = heap[0][1]
        while heap:
            price, beauty = heapq.heappop(heap)
            if price > prev_price:
                sorted_items.append((prev_price, max_beauty))
                prev_price = price
            max_beauty = max(max_beauty, beauty)
        sorted_items.append((prev_price, max_beauty))
        print(sorted_items)
        
        result = []
        for query in queries:
            pos = binary_search(sorted_items, 0, len(sorted_items) - 1, query)
            if pos >= 0:
                value = sorted_items[pos][1]
            else:
                value = 0
            result.append(value)

        return result
