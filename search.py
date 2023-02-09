import requests
from bs4 import BeautifulSoup

def find_movie_streaming_sites(movie_name):
    query = movie_name + " watch online"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    google_search = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(google_search.text, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    streaming_sites = []
    for link in links:
        if "watch" in link and "online" in link:
            if link.startswith("http"):
                streaming_sites.append(link)
    return streaming_sites

movie_name = input("Enter movie name: ")
sites = find_movie_streaming_sites(movie_name)
print("Sites where you can watch the movie:")
for site in sites:
    print(site)
