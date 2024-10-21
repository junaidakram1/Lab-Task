import unittest
from SocialNetwork import SocialNetwork, Tweet  # Import classes from social_network.py

class TestSocialNetwork(unittest.TestCase):
    def test_empty_tweet_list(self):
        sn = SocialNetwork()
        follows_graph = sn.guess_follows_graph([])
        self.assertEqual(follows_graph, {})

    def test_tweets_with_no_mentions(self):
        sn = SocialNetwork()
        tweets = [Tweet(1, 'user1', 'Hello there!', '2024-10-21')]
        follows_graph = sn.guess_follows_graph(tweets)
        self.assertEqual(follows_graph, {'user1': set()})

    def test_user_mentions(self):
        sn = SocialNetwork()
        tweets = [Tweet(1, 'user1', 'Hello @user2', '2024-10-21')]
        follows_graph = sn.guess_follows_graph(tweets)
        self.assertEqual(follows_graph['user1'], {'user2'})

    def test_multiple_mentions(self):
        sn = SocialNetwork()
        tweets = [Tweet(1, 'user1', 'Hello @user2 and @user3', '2024-10-21')]
        follows_graph = sn.guess_follows_graph(tweets)
        self.assertEqual(follows_graph['user1'], {'user2', 'user3'})

    def test_self_following_not_allowed(self):
        sn = SocialNetwork()
        tweets = [Tweet(1, 'user1', 'Hello @user1', '2024-10-21')]
        follows_graph = sn.guess_follows_graph(tweets)
        self.assertEqual(follows_graph['user1'], set())

    def test_influencers_empty_graph(self):
        sn = SocialNetwork()
        influencers = sn.influencers({})
        self.assertEqual(influencers, [])

    def test_single_user_no_followers(self):
        sn = SocialNetwork()
        follows_graph = {'user1': set()}
        influencers = sn.influencers(follows_graph)
        self.assertEqual(influencers, [])

    def test_single_influencer(self):
        sn = SocialNetwork()
        follows_graph = {'user1': {'user2'}}
        influencers = sn.influencers(follows_graph)
        self.assertEqual(influencers, ['user2'])

    def test_multiple_influencers(self):
        sn = SocialNetwork()
        follows_graph = {
            'user1': {'user2'},
            'user3': {'user2', 'user4'},
            'user4': {'user2'}
        }
        influencers = sn.influencers(follows_graph)
        # user2 should be an influencer due to the number of followers
        self.assertIn('user2', influencers)
        # Since user4 is not followed by anyone else, only user2 should be the influencer
        self.assertNotIn('user4', influencers)

    def test_equal_follower_counts(self):
        sn = SocialNetwork()
        follows_graph = {
            'user1': {'user2'},
            'user3': {'user2'},
            'user4': {'user2'}
        }
        influencers = sn.influencers(follows_graph)
        self.assertIn('user2', influencers)
        self.assertEqual(influencers.count('user2'), 1)  # user2 should be only once in the list

if __name__ == '__main__':
    unittest.main()
