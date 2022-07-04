class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        b_i = 0
        while truckSize and b_i < len(boxTypes):
            if boxTypes[b_i][0] < truckSize:
                truckSize -= boxTypes[b_i][0]
                total += boxTypes[b_i][1] * boxTypes[b_i][0]
                b_i += 1
            else:
                total += boxTypes[b_i][1] * truckSize
                truckSize = 0
        return total
