class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        A = len(arr)
        triplets = 0
        for i in range(A):
            a = 0
            for j in range(i + 1, A):
                a ^= arr[j - 1]
                b = 0
                for k in range(j, A):
                    b ^= arr[k]
                    if a == b:
                        triplets += 1
        return triplets
