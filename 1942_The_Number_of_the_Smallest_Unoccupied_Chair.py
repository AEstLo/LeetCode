class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        min_heap = []
        arrivals = {}
        leavings = defaultdict(list)
        max_time = 0
        for friend, (arrival, leaving) in enumerate(times):
            arrivals[arrival] = friend
            leavings[leaving].append(friend)
            max_time = max(max_time, arrival)

        max_chair = 0
        chairs = {}
        for time in range(1, max_time + 1):
            # leavings
            if time in leavings:
                for friend in leavings[time]:
                    heapq.heappush(min_heap, chairs[friend])
                    del chairs[friend]

            # arrivals
            if time in arrivals:
                friend = arrivals[time]
                # if we have a priority chair, we take it
                if min_heap:
                    chairs[friend] = heapq.heappop(min_heap)
                else:
                    chairs[friend] = max_chair
                    max_chair += 1
                if friend == targetFriend:
                    return chairs[friend]
        return -1
