class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champions = {i for i in range(n)}
        for edge in edges:
            if edge[1] in champions:
                champions.remove(edge[1])
        if len(champions) != 1:
            return -1
        return champions.pop()
