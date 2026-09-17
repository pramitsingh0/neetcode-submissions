class Tweet:
    def __init__(self, tweetId, timestamp):
        self.tweetId = tweetId
        self.timestamp = timestamp

class User:
    def __init__(self, userId):
        self.userId = userId
        self.tweets = []
        self.following = set()
    
    def createTweet(self, tweetId, timestamp) -> None:
        newTweet = Tweet(tweetId, timestamp)
        self.tweets.append(newTweet)
    
    def getTweets(self):
        return self.tweets

    def getTweetsLen(self):
        return len(self.tweets)
    def getIthTweet(self, i):
        return self.tweets[i] if i >= 0 and i < len(self.tweets) else Tweet(-1, -1)

    def getFollowingTweets(self):
        res = []
        for f in self.following:
            res.extend(f.getTweets())
        return res
    
        
    def follow(self, followee) -> None:
        self.following.add(followee)
    
    def unfollow(self, followee) -> None:
        if followee in self.following:
            self.following.remove(followee)

class Twitter:

    def __init__(self):
        self.users = {}
        self.timestamp = 0
    
    def getOrCreateUser(self, userId) -> User:
        if userId in self.users:
            return self.users[userId]
        else:
            newUser = User(userId)
            self.users[userId] = newUser
            return newUser

    def postTweet(self, userId: int, tweetId: int) -> None:
        userObj = self.getOrCreateUser(userId)
        self.timestamp += 1
        userObj.createTweet(tweetId, self.timestamp)

    def getNewsFeed(self, userId: int) -> List[int]:
        userObj = self.getOrCreateUser(userId)
        candidates = list(userObj.following) + [userObj]
        heap = []
        feed = []
        for c in candidates:
            cNumTweets = c.getTweetsLen()
            latestTweet = c.getIthTweet(cNumTweets - 1)
            if latestTweet.tweetId >= 0:
                heap.append([latestTweet.timestamp, latestTweet.tweetId, c, cNumTweets - 1])
        heapq.heapify_max(heap)
        while heap and len(feed) < 10:
            tweetTimestamp, tweetId, tweeterUser, pointer = heapq.heappop_max(heap)
            feed.append(tweetId)
            latestTweet = tweeterUser.getIthTweet(pointer - 1)
            if latestTweet.tweetId >= 0:
                heapq.heappush_max(heap, [latestTweet.timestamp, latestTweet.tweetId, tweeterUser, pointer - 1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        followerObj = self.getOrCreateUser(followerId)
        followeeObj = self.getOrCreateUser(followeeId)
        followerObj.follow(followeeObj)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerObj = self.getOrCreateUser(followerId)
        followeeObj = self.getOrCreateUser(followeeId)
        followerObj.unfollow(followeeObj)
        
