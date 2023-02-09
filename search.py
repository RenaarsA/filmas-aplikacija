import requests
from bs4 import BeautifulSoup

def find_movie_on_soap2day(movie_name):
    query = movie_name + " site:soap2day.to"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    soap2day_search = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(soap2day_search.text, "html.parser")
    movie_link = soup.find("a", href=lambda x: "soap2day.to" in x)
    if movie_link:
        return movie_link["href"]
    else:
        return None

movie_name = input("Enter movie name: ")
link = find_movie_on_soap2day(movie_name)
if link:
    print(f"Link to the movie '{movie_name}' on soap2day: {link}")
else:
    print(f"Movie '{movie_name}' not found on soap2day.")
