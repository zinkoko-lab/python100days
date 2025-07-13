from newsapi import NewsApiClient
from pprint import pprint

# Init
newsapi = NewsApiClient(api_key="01965599566d41f98d5d42a80b2bc659")

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(
#     q="bitcoin",
#     sources="bbc-news,the-verge",
#     language="en",
# )

# /v2/everything
# all_articles = newsapi.get_everything(
#     q="bitcoin",
#     sources="bbc-news,the-verge",
#     domains="bbc.co.uk,techcrunch.com",
#     from_param="2017-12-01",
#     to="2017-12-12",
#     language="en",
#     sort_by="relevancy",
#     page=2,
# )

# /v2/top-headlines/sources
sources = newsapi.get_sources()
pprint(sources)
