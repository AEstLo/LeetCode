class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        steps = time % ((n-1) * 2)
        asc = True
        current = 1
        while steps:
            if asc:
                current += 1
                if current == n:
                    asc = False
            else:
                current -= 1
                if current == 1:
                    asc = True
            steps -= 1
        return current
