class Twitter:

    def __init__(self):
        # follow relationship
        # postTweet relationship
        # fetch relationship, tweetId is part of the time
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        if userId not in self.following:
            self.following[userId] = []
            self.following[userId].append(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # get 10 last tweets from each its followee
        tempTweets = []
        for followee in self.following[userId]:
            tweets = self.tweets[followee]
            size = min(len(tweets), 10)
            # print(tweets)
            for j in range(len(tweets)-1, len(tweets)-size-1, -1):
                if tweets[j] not in tempTweets:
                    tempTweets.append(tweets[j])
            # print(tweets, tempTweets)
        heapq.heapify(tempTweets)
        res = []
        size = min(10, len(tempTweets))
        res = []
        for i in range(size):
            res.append(heapq.heappop(tempTweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = []
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(followerId, followeeId)
        # print(self.following)
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
            # print(self.following)
            
        
