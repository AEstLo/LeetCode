from collections import defaultdict


class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        R = len(ring)
        K = len(key)
        INF = 10 ** 20

        indices = defaultdict(list)
        for index, c in enumerate(ring):
            indices[c].append(index)

        memo = {}

        def recursion(k_index, r_index):
            if k_index == K:
                return 0
            memo_tuple = (k_index, r_index)
            if memo_tuple in memo:
                return memo[memo_tuple]
            min_steps = INF
            for i in indices[key[k_index]]:
                if i > r_index:
                    go_right = i - r_index
                    go_left = R + r_index - i
                else:
                    go_right = R + i - r_index
                    go_left = r_index - i
                steps = min(go_left, go_right)
                min_steps = min(
                    min_steps,
                    steps + recursion(k_index + 1, i),
                )
            memo[memo_tuple] = min_steps + 1
            return min_steps + 1

        return recursion(0, 0)
