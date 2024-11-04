class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        current = word[0]
        acum = 1
        for char in word[1:]:
            if char != current or acum > 8:
                result.append(str(acum))
                result.append(current)
                current = char
                acum = 0
            acum += 1
        result.append(str(acum))
        result.append(current)
        return ''.join(result)
