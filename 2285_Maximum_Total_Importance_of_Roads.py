class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        node_degrees = [0 for i in range(n)]
        for a, b in roads:
            node_degrees[a] += 1
            node_degrees[b] += 1
        
        heap = []
        for i in range(n):
            heapq.heappush(heap, (node_degrees[i], i))

        importances = [0 for i in range(n)]
        for importance in range(1, n + 1):
            degree, pos = heapq.heappop(heap)
            if degree:
                importances[pos] += importance
        total = 0
        for a, b in roads:
            total += importances[a] + importances[b]
        return total
