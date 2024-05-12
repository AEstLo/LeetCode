class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        total = 0
        first_char = ord('a')
        mask = 0
        freq = {0: 1}

        for w in word:
            bit = ord(w) - first_char
            num = 1 << bit
            mask ^= num

            if mask in freq:
                total += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1

            for odd_c in range(10):
                if mask ^ (1 << odd_c) in freq:
                    total += freq[mask ^ (1 << odd_c)]

        return total
