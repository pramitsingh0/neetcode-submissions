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
        userTweets = userObj.getTweets()
        userFollowingTweets = userObj.getFollowingTweets()
        allTweets = userTweets + userFollowingTweets

        # timestamp -> tweet map
        ttMap = {}
        temp = []
        for t in allTweets:
            ttMap[t.timestamp] = t.tweetId
            temp.append(t.timestamp)
        heapq.heapify_max(temp)
        feed = []
        i = 0
        while temp and i < 10:
            tweet = ttMap[heapq.heappop_max(temp)]
            feed.append(tweet)
            i += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        followerObj = self.getOrCreateUser(followerId)
        followeeObj = self.getOrCreateUser(followeeId)
        followerObj.follow(followeeObj)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerObj = self.getOrCreateUser(followerId)
        followeeObj = self.getOrCreateUser(followeeId)
        followerObj.unfollow(followeeObj)
        
