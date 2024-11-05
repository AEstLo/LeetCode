class Solution:
    def minOperations(self, s: str) -> int:
        # Two options: Either s[0] is 1 or 0, result is the minimum
        operations_zero = 0
        operations_one = 0
        n = len(s)
        l = list(s)
        # s[0] = 0
        prev = '1'
        i = 0
        while i < n:
            if l[i] == prev:
                operations_zero += 1
                if l[i] == '0':
                    l[i] = '1'
                else:
                    l[i] = '0'
            prev = l[i]
            i += 1

        # s[0] = 1
        l = list(s)
        prev = '0'
        i = 0
        while i < n:
            if l[i] == prev:
                operations_one += 1
                if l[i] == '0':
                    l[i] = '1'
                else:
                    l[i] = '0'
            prev = l[i]
            i += 1
        return min(operations_zero, operations_one)
