class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Being N the number of strs and K the number of characters of the longest string
        # Time: O(N * K)
        # Space: O(N * K)
        ord_a = ord('a')
        num_characters = ord('z') - ord_a + 1
        get_key_list = [0] * num_characters
        res = []

        def setZero():
            for i in range(num_characters):
                get_key_list[i] = 0
            res.clear()

        def getKey(string):
            setZero()
            for c in string:
                get_key_list[ord(c) - ord_a] += 1
            for i in range(num_characters):
                res.append(f'{chr(i + ord_a)}{get_key_list[i]}')
            return ''.join(res)

        result = collections.defaultdict(list)
        for s in strs:
            result[getKey(s)].append(s)
        return list(result.values())
