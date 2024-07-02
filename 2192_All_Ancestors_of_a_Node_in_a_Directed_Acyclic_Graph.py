class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        linked_to = []
        dependencies = []
        result = []
        no_dep = set()
        for i in range(n):
            dependencies.append(0)
            linked_to.append(set())
            result.append([])
            no_dep.add(i)
        for a, b in edges:
            dependencies[b] += 1
            linked_to[a].add(b)
            if b in no_dep:
                no_dep.remove(b)

        topological_order = []
        while no_dep:
            node = no_dep.pop()
            topological_order.append(node)
            for num in linked_to[node]:
                dependencies[num] -= 1
                if not dependencies[num]:
                    no_dep.add(num)

        # Initialize the result list and set list for storing ancestors
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]

        # Fill the set list with ancestors using the topological order
        for node in topological_order:
            for neighbor in linked_to[node]:
                # Add immediate parent, and other ancestors.
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        # Convert sets to lists and sort them
        for i in range(n):
            for node in range(n):
                if node == i:
                    continue
                if node in ancestors_set_list[i]:
                    ancestors_list[i].append(node)
        return ancestors_list
