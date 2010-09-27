import reddit

unsubscribe = ["reddit.com",
               "pics", "wtf", "funny",
               "science", "atheism", "politics",
               "technology"]

subscribe = ["humor", "offbeat",
             "worldnews", "news",
             "hardware", "software", "computing", "netsec", "buildapc",
             "listentothis", "radioreddit",
             "tldr",
             "depthhub", "foodforthought", "criticism", "designthought",
                    "truereddit",
             "favors", "iwanttolearn", "bestof", "worstof"]

def main():
    r = reddit.Reddit()
    r.login()

    for subreddit in unsubscribe:
        r.get_subreddit(subreddit).unsubscribe()
    for subreddit in subscribe:
        r.get_subreddit(subreddit).subscribe()

if __name__ == "__main__":
    main()
