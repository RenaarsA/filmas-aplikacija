import tkinter as tk
import webbrowser

def search_movie():
    video_name = movie_entry.get()
    query = video_name + " site:soap2day.id"
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_anime():
    anime_name = anime_entry.get()
    query = anime_name + " site:9anime.to"
    webbrowser.open(f"https://www.google.com/search?q={query}")

    

app = tk.Tk()
app.geometry('350x150')
app.title("Movie Search")

movie_label = tk.Label(text="Enter movie name:").grid(row=1,column=2)


anime_label= tk.Label(text="Enter anime name:").grid(row=2,column=2)


movie_entry = tk.Entry()
movie_entry.grid(row=1,column=3)


anime_entry = tk.Entry()
anime_entry.grid(row=2,column=3)


search_button_movie = tk.Button(text="Search Movie", command=search_movie).grid(row=1,column=4)
search_button_anime = tk.Button(text="Search Anime", command=search_anime).grid(row=2,column=4)


app.mainloop()