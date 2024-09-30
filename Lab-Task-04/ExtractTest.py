import unittest
from datetime import datetime
from Extract import Tweet, get_timespan, get_mentioned_users

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.tweet1 = Tweet(1, "alyssa", "is it reasonable to talk about rivest so much?", "2016-02-17T10:00:00Z")
        self.tweet2 = Tweet(2, "bbitdiddle", "rivest talk in 30 minutes @hype", "2016-02-17T11:00:00Z")
    
    def test_get_timespan_two_tweets(self):
        start, end = get_timespan([self.tweet1, self.tweet2])
        self.assertEqual(start, datetime.fromisoformat("2016-02-17T10:00:00+00:00"))
        self.assertEqual(end, datetime.fromisoformat("2016-02-17T11:00:00+00:00"))
    
    def test_get_mentioned_users_no_mention(self):
        mentioned_users = get_mentioned_users([self.tweet1])
        self.assertEqual(mentioned_users, set())
    
    def test_get_mentioned_users_with_mentions(self):
        mentioned_users = get_mentioned_users([self.tweet2])
        self.assertEqual(mentioned_users, {"hype"})

if __name__ == '__main__':
    unittest.main()
