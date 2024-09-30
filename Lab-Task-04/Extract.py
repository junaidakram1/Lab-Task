from datetime import datetime
from typing import List, Set, Tuple

class Tweet:
    def __init__(self, id: int, username: str, content: str, timestamp: str):
        self.id = id
        self.username = username
        self.content = content
        self.timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

def get_timespan(tweets: List[Tweet]) -> Tuple[datetime, datetime]:
    start = min(tweet.timestamp for tweet in tweets)
    end = max(tweet.timestamp for tweet in tweets)
    return start, end

def get_mentioned_users(tweets: List[Tweet]) -> Set[str]:
    mentioned_users = set()
    for tweet in tweets:
        words = tweet.content.split()
        for word in words:
            if word.startswith("@"):
                mentioned_users.add(word[1:].lower())  # Add without the '@' and in lowercase
    return mentioned_users
