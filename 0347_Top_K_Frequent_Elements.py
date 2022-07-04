class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequenceDict = {}
        for num in nums:
            if num not in frequenceDict:
                frequenceDict[num] = 1
            else:
                frequenceDict[num] += 1
        ret = []
        for key, val in sorted(frequenceDict.items(), key=lambda x: x[1], reverse=True):
            ret.append(key)
            k -= 1
            if not k:
                return ret
        return ret
