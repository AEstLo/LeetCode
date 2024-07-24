class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_dict = {i: j for i, j in enumerate(mapping)}

        def getNewCode(num):
            if num == 0:
                return mapping_dict[num]
            result = 0
            i = 0
            while num:
                result += mapping_dict[(num % 10)] * 10**i
                i += 1
                num //= 10
            return result

        result_map = defaultdict(list)
        for number in nums:
            result_map[getNewCode(number)].append(number)

        result = []
        for k in sorted(result_map.keys()):
            for number in result_map[k]:
                result.append(number)
        return result
