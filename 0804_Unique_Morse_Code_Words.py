class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time: O(N*K)
        # Space: O(N*K)
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_dict = {}
        for char in range(ord('a'), ord('z') + 1):
            morse_dict[chr(char)] = morse[char - ord('a')]

        representations = set()
        for word in words:
            morse_word = ''.join([morse_dict[char] for char in word])
            representations.add(morse_word)
        return len(representations)

# Runtime: 39 ms, faster than 89.66% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.8 MB, less than 75.48% of Python3 online submissions for Unique Morse Code Words.
