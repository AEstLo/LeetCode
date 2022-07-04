class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        target_pos = n - 1
        graph = {}
        for i in range(n):
            if arr[i] not in graph:
                graph[arr[i]] = []
            graph[arr[i]].append(i)

        q = []
        q2 = []
        q.append((0, 0))
        visited = set()
        while q:

            for pos, jumps in q:
                if pos == target_pos:
                    return jumps
                if pos not in visited:
                    visited.add(pos)
                    for neighbor_pos in graph[arr[pos]]:
                        if neighbor_pos not in visited:
                            q2.append((neighbor_pos, jumps + 1))
                    graph[arr[pos]].clear()
                    for neighbor_pos in (pos - 1, pos + 1):
                        if 0 <= neighbor_pos < len(arr) and neighbor_pos not in visited:
                            q2.append((neighbor_pos, jumps + 1))
            q.clear()
            q, q2 = q2, q
        return n - 1
