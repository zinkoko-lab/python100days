import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empireonline_movies = response.text
soup = BeautifulSoup(empireonline_movies, "html.parser")

movie_name_tags = soup.findAll(name="h3", class_="title")
movie_titles = [tag.getText() for tag in movie_name_tags][::-1]
# print(movie_titles)

with open(file="movies.txt", mode="w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
