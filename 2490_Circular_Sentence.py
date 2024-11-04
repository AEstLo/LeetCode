class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        pos = 1
        while pos < len(sentence) - 1:
            while pos < len(sentence) - 1 and sentence[pos] != ' ':
                pos += 1
            if pos < len(sentence) - 1:
                if sentence[pos-1] != sentence[pos+1]:
                    return False
            pos += 1
        return True
