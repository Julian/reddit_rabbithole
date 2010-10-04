from pprint import pprint

from reddit_api import reddit

def multiplied_front_page(reddit_session, multipliers):
    front_page = reddit_session.get_front_page(limit=10)

    for subm in front_page:
        subm._score = subm.score * multipliers.get(subm.subreddit, 1)

    return sorted(front_page, key=lambda subm: subm._score, reverse=True)

def demo():
    r = reddit.Reddit()
    r.login()

    print "Front Page Multiplier Demo\n"

    multipliers = {"pics" : 1,
                   "funny" : 1,
                   "design" : 8,
                   "amatureradio" : 40,
                   "designthought" : 2,
                   "python" : 2}

    print "Multipliers:"
    pprint(multipliers)

    print "\nNew front page:"
    for s in multiplied_front_page(r, multipliers):
        print unicode(s)

if __name__ == "__main__":
    demo()
