import twitter
import constants


def get_tweets(twitter_user_name="realdonaldtrump"):
    return_string = ""

    api = twitter.Api(consumer_key=constants.consumer_key, consumer_secret=constants.consumer_secret,
                      access_token_key=constants.access_token_key, access_token_secret=constants.access_token_secret)
    statuses = api.GetUserTimeline(screen_name=twitter_user_name, count=300)
    for status in statuses:
        status = status.AsDict()
        status_text = status.get("text")
        if status_text[0:2] != "RT":
            return_string += status_text

    file = open("analyze.txt", "w")
    file.write(return_string)
    file.close()

    return return_string


if __name__ == "__main__":
    get_tweets()
