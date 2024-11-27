"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newNodes = {}

        def dfs(n):
            if n in newNodes:
                return newNodes[n]
            newNodes[n] = Node(n.val)
            for neighbor in n.neighbors:
                newNodes[n].neighbors.append(dfs(neighbor))
            return newNodes[n]
        return dfs(node)
