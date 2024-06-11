class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = [-1] * len(arr1)
        counter = defaultdict(int)
        for num in arr1:
            counter[num] += 1
        
        i = 0
        for num in arr2:
            while counter[num] > 0:
                result[i] = num
                counter[num] -= 1
                i += 1
            del counter[num]
        
        buckets = [0] * 1001
        for k in counter:
            buckets[k] = counter[k]
        
        for j in range(1001):
            while buckets[j] > 0:
                result[i] = j
                buckets[j] -= 1
                i += 1

        return result
