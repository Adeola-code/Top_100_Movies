import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_webpage = response.text

soup=BeautifulSoup(empire_webpage, "html.parser")
all_movies=soup.find_all("h3",class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles= [movie.getText() for movie in all_movies]
movies=movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

