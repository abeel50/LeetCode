class User:
    def __init__(self, id):
        self.id = id
        self.following = OrderedDict()    
    
    def followUser(self, followeId):
        self.following[followeId] = True
        
    def unFollowUser(self, followeId):
        if followeId in self.following:
            del self.following[followeId]
        
        
class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = OrderedDict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
            self.users[userId].followUser(userId)
        self.tweets[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId not in self.users:
            return feed
        following = self.users[userId].following.keys()
        for t, u in reversed(self.tweets.items()):
            if u in following:
                feed.append(t)
                if len(feed) == 10:
                    break
        return feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
            self.users[followerId].followUser(followerId)

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
            self.users[followeeId].followUser(followeeId)

        self.users[followerId].followUser(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
         self.users[followerId].unFollowUser(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)