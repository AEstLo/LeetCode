class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = []
        prev = ''
        prev_prev = ''
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))
        while heap:
            next_char = heapq.heappop(heap)
            if prev != next_char[1] or prev_prev != next_char[1]:
                prev_prev = prev
                prev = next_char[1]
                if next_char[0] + 1 < 0:
                    heapq.heappush(heap, (next_char[0] + 1, next_char[1]))
                output.append(next_char[1])
                continue
            if heap:
                next_next_char = heapq.heappop(heap)
                heapq.heappush(heap, next_char)
                prev = next_next_char[1]
                if next_next_char[0] + 1 < 0:
                    heapq.heappush(heap, (next_next_char[0] + 1, next_next_char[1]))
                output.append(next_next_char[1])

        return ''.join(output)
