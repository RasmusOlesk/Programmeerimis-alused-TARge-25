class Tweet:

    hash_tags = {}
    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets
        self.hash_tags = list(filter(lambda word: word.startswith("#"), content.split()))
        for tag in self.hash_tags:
            Tweet.hash_tags[tag] = Tweet.hash_tags.get(tag, 0) + 1

    def get_growth_rate(self) -> float:
        """Return tweets growth rate.
        Bigger is better"""
        return self.retweets / self.time

    def __gt__(self, other):
        if isinstance(other, Tweet):
            if self.retweets == other.retweets:
                return self.time < other.time
            return self.retweets > other.retweets
        return False

    def __repr__(self):
        return f"Tweet({self.user}, {self.content}, {self.time}, {self.retweets})"