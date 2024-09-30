from datetime import datetime

class Tweet:
    def __init__(self, tweet_id, username, text, created_at, user_screen_name):
        self.id = tweet_id
        self.username = username
        self.text = text
        self.created_at = created_at
        self.user_screen_name = user_screen_name

    def __repr__(self):
        return f"Tweet(id={self.id}, username='{self.username}', text='{self.text}', created_at='{self.created_at}', user_screen_name='{self.user_screen_name}')"

class Timespan:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Filter:
    @staticmethod
    def writtenBy(tweets, username):
        """Filter tweets written by a specific username."""
        return [tweet for tweet in tweets if tweet.username == username]

    @staticmethod
    def inTimespan(tweets, timespan):
        """Filter tweets within a specified timespan."""
        return [tweet for tweet in tweets if timespan.start <= tweet.created_at <= timespan.end]

    @staticmethod
    def containing(tweets, keywords):
        """Filter tweets that contain specific keywords."""
        return [tweet for tweet in tweets if any(keyword in tweet.text for keyword in keywords)]
