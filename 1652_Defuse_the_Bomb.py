class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        sums = [0] * n
        if k == 0:
            return sums
        if k < 0:
            sum_elems = sum(code[i] for i in range(n + k, n))
        else:
            sum_elems = sum(code[i] for i in range(1, k + 1))
        for i in range(n):
            sums[i] = sum_elems
            if k < 0:
                sum_elems += code[i]
                sum_elems -= code[(i + k) % n]
            else:
                sum_elems -= code[(i + 1) % n]
                sum_elems += code[(i + 1 + k) % n]
        return sums
