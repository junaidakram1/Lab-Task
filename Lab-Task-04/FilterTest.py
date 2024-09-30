import unittest
from datetime import datetime
from Filter import Tweet, Filter, Timespan

class FilterTest(unittest.TestCase):
    d1 = datetime.fromisoformat("2016-02-17T10:00:00")
    d2 = datetime.fromisoformat("2016-02-17T11:00:00")

    tweet1 = Tweet(1, "alyssa", "is it reasonable to talk about rivest so much?", d1, "alyssa_screen")
    tweet2 = Tweet(2, "bbitdiddle", "rivest talk in 30 minutes #hype", d2, "bbitdiddle_screen")

    def test_written_by_multiple_tweets_single_result(self):
        writtenBy = Filter.writtenBy([self.tweet1, self.tweet2], "alyssa")
        self.assertEqual(len(writtenBy), 1)
        self.assertIn(self.tweet1, writtenBy)

    def test_in_timespan_multiple_tweets_multiple_results(self):
        testStart = datetime.fromisoformat("2016-02-17T09:00:00")
        testEnd = datetime.fromisoformat("2016-02-17T12:00:00")
        timespan = Timespan(testStart, testEnd)

        inTimespan = Filter.inTimespan([self.tweet1, self.tweet2], timespan)
        self.assertFalse(len(inTimespan) == 0)
        self.assertIn(self.tweet1, inTimespan)
        self.assertIn(self.tweet2, inTimespan)

    def test_containing(self):
        containing = Filter.containing([self.tweet1, self.tweet2], ["talk"])
        self.assertFalse(len(containing) == 0)
        self.assertIn(self.tweet1, containing)
        self.assertIn(self.tweet2, containing)

if __name__ == '__main__':
    unittest.main()
