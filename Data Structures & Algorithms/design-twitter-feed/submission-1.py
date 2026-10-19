class Twitter:
    
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        
        if not userId in self.tweets:
            self.tweets[userId] = []
            
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following.get(userId, set()) | {userId}
        
        allTweets = []
        for u in users:
            allTweets.extend(self.tweets.get(u, []))
            
        allTweets.sort(key=lambda tweet: tweet[0], reverse=True)
        
        return [tweet[1] for tweet in allTweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)