class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        offset_char = ord('a')
        W = len(words)

        def get_score(word, counter):
            result = 0
            for char in word:
                if char not in counter or counter[char] <= 0:
                    return 0
                counter[char] -= 1
                result += score[ord(char) - offset_char]
            return result


        def helper(index, counter, total):
            print(index, counter, total)
            if index == W:
                return total
            # skip the word
            skip_result = helper(index + 1, counter, total)
            # include the word
            copy_counter = deepcopy(counter)
            word_score = get_score(words[index], copy_counter)
            if word_score == 0:
                return skip_result
            include_result = helper(index + 1, copy_counter, total + word_score)
            return max(skip_result, include_result)


        counter = Counter(letters)
        return helper(0, counter, 0)
