import requests
from bs4 import BeautifulSoup

# Static practice website
# resoponse = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

# Live Website (will change over time)
response = requests.get("https://news.ycombinator.com/news")

y_combinator_html = response.text

soup = BeautifulSoup(y_combinator_html, "html.parser")

# Getting lists of article name, article links and article upvotes
article_tags = soup.findAll(name="span", class_="titleline")
article_texts = [tag.getText() for tag in article_tags]
article_links = [tag.a.get("href") for tag in article_tags]
article_upvote_tags = soup.findAll(name="span", class_="score")
article_scores = [int(tag.getText().split()[0]) for tag in article_upvote_tags]

# print(article_texts)
# print(article_links)
# print(article_scores)

max_score = max(article_scores)
max_score_index = article_scores.index(max_score)

print(
    "The title and link for the story with the highest number of upvotes is as follow..."
)
print(f"Title: {article_texts[max_score_index]}")
print(f"Link: {article_links[max_score_index]}")
print(f"Number of upvotes: {max_score}")
