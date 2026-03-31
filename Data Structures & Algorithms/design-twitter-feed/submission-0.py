class Twitter:

    def __init__(self):
        self.followMap = {}
        self.tweetmap = {}
        self.count = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)

        self.count += 1
        if userId not in self.tweetmap.keys():
           self.tweetmap[userId] = []
        self.tweetmap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = []
        if userId in self.followMap.keys():
            users = list(self.followMap[userId])
            for user in users:
                if user in self.tweetmap.keys():
                    newsfeed.extend(self.tweetmap[user])
        largest = heapq.nlargest(10 , newsfeed)
        return [tweetId for time, tweetId in largest]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followerId)

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap.keys() and followerId != followeeId:
            self.followMap[followerId].discard(followeeId)