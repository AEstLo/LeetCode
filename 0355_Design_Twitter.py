class TwitterMsg:

    def __init__(self, userId: int, tweetId: int):
        self.userId = userId
        self.tweetID = tweetId


class Twitter:

    def __init__(self):
        # Time: O(1)
        self.messages = []
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time: O(1)
        msg = TwitterMsg(userId, tweetId)
        self.messages.append(msg)

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time: O(N) --> being N the number of messages
        news = []
        i = len(self.messages) - 1
        while i >= 0 and len(news) < 10:
            msg = self.messages[i]
            if userId in self.followers[msg.userId] or userId == msg.userId:
                news.append(msg.tweetID)
            i -= 1
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1)
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1)
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Runtime: 48 ms, faster than 49.60% of Python3 online submissions for Design Twitter.
# Memory Usage: 14 MB, less than 65.01% of Python3 online submissions for Design Twitter.
