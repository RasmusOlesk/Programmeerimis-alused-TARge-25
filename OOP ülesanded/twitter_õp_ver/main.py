from twitter import Tweet

def find_fastest_growing(tweets: list) -> Tweet:
    return max(tweets, key=lambda t: t.retweets / t.time)


def sort_by_popularity(tweets: list) -> list:
    return sorted(tweets, key=lambda t: (-t.retweets, t.time))


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    return list(filter(lambda tweet: hashtag in tweet.hash_tags, tweets))


def extract_hashtags(text: str) -> list:
    hashtags = []
    i = 0
    while i < len(text):
        if text[i] == "#":
            j = i + 1
            while j < len(text) and text[j].isalnum():
                j += 1
            hashtags.append(text[i:j])
            i = j
        else:
            i += 1
    return hashtags


def sort_hashtags_by_popularity(tweets: list[Tweet]) -> list[str]:
    """hash_tags_by_count = {}
    for tweet in tweets:
        for tag in tweet.hash_tags:
            hash_tags_by_count[tag] = hash_tags_by_count.get(tag, 0) + 1
    counts_with_hash_tags = {}
    sorted_by_value = dict(sorted(hash_tags_by_count.items(), key=lambda item: item[1]))
    for tag, count in hash_tags_by_count.items():
        count_list = counts_with_hash_tags.get(count, [])
        count_list.append(tag)
        counts_with_hash_tags[count] = count_list

    result_tags = []
    for count, tags in counts_with_hash_tags.items():
        tags.sort()
        result_tags += tags
    return result_tags

    # return list(map(lambda k_v: k_v[0], sorted_by_value))"""

    hash_tags_by_count = {}
    for tweet in tweets:
        for tag in tweet.hash_tags:
            hash_tags_by_count[tag] = hash_tags_by_count.get(tag, 0) + tweet.retweets
    return list(map(lambda item: item[0], sorted(hash_tags_by_count, key=hash_tags_by_count.get, reverse=True)))


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"


    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
