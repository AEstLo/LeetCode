class Solution:
    def minimumSteps(self, s: str) -> int:
        BLACK = '1'
        WHITE = '0'
        steps = 0
        black_count = 0
        for char in s:
            if char == WHITE:
                steps += black_count
            else:
                black_count += 1

        return steps
