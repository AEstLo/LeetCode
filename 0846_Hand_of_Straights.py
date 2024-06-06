class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        heap = []
        for h in counter.keys():
            heappush(heap, h)
        while heap:
            while heap and counter[heap[0]] <= 0:
                heappop(heap)
            if not heap:
                break
            i = heap[0]
            counter[i] -= 1
            i += 1
            elements_found = 1
            while elements_found < groupSize:
                if counter[i] <= 0:
                    return False
                counter[i] -= 1
                i += 1
                elements_found += 1

        return True if all(v == 0 for v in counter.values()) else False
