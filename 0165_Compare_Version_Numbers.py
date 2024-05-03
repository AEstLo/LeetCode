class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def getNextValue(from_position: int, version: str) -> tuple[int, int]:
            val = 0
            while from_position < len(version) and version[from_position] != ".":
                val *= 10
                val += int(version[from_position])
                from_position += 1
            return val, from_position + 1

        v1_i = 0
        v1_value = 0
        v2_i = 0
        v2_value = 0
        while v1_i < len(version1) or v2_i < len(version2):
            v1_value, v1_i = getNextValue(v1_i, version1)
            v2_value, v2_i = getNextValue(v2_i, version2)
            if v1_value < v2_value:
                return -1
            if v1_value > v2_value:
                return 1
        return 0
