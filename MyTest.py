import feedparser

rssURLs = {
    "rss.slashdot.org": "http://rss.slashdot.org/Slashdot/slashdotMain",
    "finance.yahoo.com": "https://finance.yahoo.com/rss/",
    "stackoverflow.com": "https://stackoverflow.com/feeds",
    "news.ycombinator.com": "https://news.ycombinator.com/rss",
}

for key, url in rssURLs.items():
    print(f"Processing {key}:{url}")
    d = feedparser.parse(url)
    print(d)

print('sof')
