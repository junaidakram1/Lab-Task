class Tweet:
    def __init__(self, tweet_id, author, content, timestamp):
        self.tweet_id = tweet_id
        self.author = author
        self.content = content
        self.timestamp = timestamp

class SocialNetwork:
    @staticmethod
    def guess_follows_graph(tweets):
        follows_graph = {}
        
        for tweet in tweets:
            author = tweet.author.lower()
            # Initialize the author's set if not already present
            if author not in follows_graph:
                follows_graph[author] = set()
            
            # Extract mentions from the tweet content
            mentions = [word[1:].lower() for word in tweet.content.split() if word.startswith('@')]
            for mention in mentions:
                if mention != author:  # A user cannot follow themselves
                    follows_graph[author].add(mention)
        
        return follows_graph

    @staticmethod
    def influencers(follows_graph):
        follower_count = {}

        # Count followers for each user
        for user, following in follows_graph.items():
            for followed_user in following:
                # Increase the follower count for each followed user
                follower_count[followed_user] = follower_count.get(followed_user, 0) + 1

        # If no followers are found, return an empty list
        if not follower_count:
            return []

        # Find the maximum follower count
        max_followers = max(follower_count.values())

        # Collect users with the maximum follower count
        top_influencers = [user for user, count in follower_count.items() if count == max_followers]

        return top_influencers
