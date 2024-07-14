class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            prio = "ba"
            prio_score = y
            low_score = x
        else:
            prio = "ab"
            prio_score = x
            low_score = y
        gain = 0
        l = []
        i = 0
        while i < len(s):
            l.append(s[i])
            if len(l) > 1 and l[-1] == prio[1] and l[-2] == prio[0]:
                l.pop()
                l.pop()
                gain += prio_score
            i += 1
        
        l2 = []
        i = 0
        while i < len(l):
            l2.append(l[i])
            if len(l2) > 1 and l2[-1] == prio[0] and l2[-2] == prio[1]:
                l2.pop()
                l2.pop()
                gain += low_score
            i += 1

        return gain
