class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []
        adjancency = {i: [i+1] for i in range(n)}
        for query in queries:
            adjancency[query[0]].append(query[1])
        
            q = deque([(0, 0)])
            visited = {0}
            while q:
                node, distance = q.pop()
                if node == n - 1:
                    result.append(distance)
                    break
                for destiny in adjancency[node]:
                    if destiny not in visited:
                        q.appendleft((destiny, distance + 1))
                        visited.add(destiny)

        return result
