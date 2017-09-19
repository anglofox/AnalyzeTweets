import matplotlib.pyplot as plt
import requests
from pandas import Series

import constants
import get_tweets


def go_through_category(category_name, category):
    values = {}
    print(category_name)
    for trait in category:
        values[trait.get("name")] = trait.get("percentile")
        print("{} - {}".format(trait.get("name"), trait.get("percentile")))
    return values


def analyze_personality(user="realdonaldtrump"):
    get_tweets.get_tweets(user)

    headers = {
        'Content-Type': 'text/plain;charset=utf-8',
    }

    params = (
        ('version', '2016-10-20'),
    )
    data = open('./analyze.txt', 'rb').read()

    return_val = requests.post(constants.watson_url + "/v3/profile", headers=headers, params=params, data=data,
                               auth=(constants.watson_username, constants.password))

    json_str = return_val.json()

    needs = json_str.get("needs")
    personality = json_str.get("personality")
    values = json_str.get("values")

    return needs, personality, values


if __name__ == "__main__":
    traits = analyze_personality()

    needs = go_through_category("NEEDS", traits[0])
    series = Series(list(needs.values()))
    series.plot(kind="bar", ylim=(0, 1))
    plt.savefig("needs.jpg")
    plt.show()
    print("_______________________________________")

    personality = go_through_category("PERSONALITY", traits[1])
    series = Series(list(personality.values()))
    plt.savefig("personality.jpg")
    series.plot(kind="bar", ylim=(0, 1))
    plt.show()

    print("_______________________________________")

    values = go_through_category("VALUES", traits[2])
    series = Series(list(values.values()))
    plt.savefig("values.jpg")
    series.plot(kind="bar", ylim=(0, 1))
    plt.show()
