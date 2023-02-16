from cgitb import text
import tkinter as tk
import webbrowser
from tkinter import Label, Toplevel, Entry, Button
import random
import tkinter.scrolledtext as scrolledtext
import pyperclip




app = tk.Tk()
app.title('Movie app')
app.eval('tk::PlaceWindow . center')
app.geometry('500x600')
label = Label(app)

def app1():
    def search_movie():
        video_name = movie_entry.get()
        query = video_name + " site:soap2day.id"
        webbrowser.open(f"https://www.google.com/search?q={query}")

    
    def search_anime():
        anime_name = anime_entry.get()
        query = anime_name + " site:9anime.to"
        webbrowser.open(f"https://www.google.com/search?q={query}")

    app = tk.Tk()
    app.title("Movie List")

    movie_label = tk.Label(app,text="Enter movie name:").grid(row=1,column=2)
    anime_label= tk.Label(app,text="Enter anime name:").grid(row=2,column=2)

    
    movie_entry = tk.Entry(app)
    movie_entry.grid(row=1,column=3)

    anime_entry = tk.Entry(app)
    anime_entry.grid(row=2,column=3)

    search_button_movie = tk.Button(app,text="Search Movie", command=search_movie).grid(row=1,column=4)
    search_button_anime = tk.Button(app,text="Search Anime", command=search_anime).grid(row=2,column=4)



btn = tk.Button(app,text='Search Movie', command=app1).grid(row=2,column=2)

def randomapp():
    def save_to_file():
        text = movie_entry.get()
        with open("movies.txt", "a") as f:
            f.write(text + "\n")
        movie_entry.delete(0, tk.END)

    def choose_random_movie():
        with open("movies.txt") as f:
            movies = f.read().splitlines()
        if movies:
            chosen_movie = random.choice(movies)
            #result_label.config(text=f"The randomly chosen movie is:\n{chosen_movie}")
            result_label.config(text=f"{chosen_movie}")
        else:
            result_label.config(text="No movies in the list yet!")
    
    def copy_result():
        result_text = result_label.cget("text")
        pyperclip.copy(result_text)
    

    root = tk.Tk()
    root.title("Movie List")
    root.geometry('250x150')

    movie_label = tk.Label(root, text="Enter a movie:")
    movie_entry = tk.Entry(root)
    movie_button = tk.Button(root, text="Add to list", command=save_to_file)

    random_label = tk.Label(root, text="Click to choose a random movie:")
    random_button = tk.Button(root, text="Random", command=choose_random_movie)

    
    result_frame = tk.Frame(root)
    result_frame.pack(side="bottom")

    
    result_label = tk.Label(result_frame, text="")
    result_label.pack(side="left")

    copy_button = tk.Button(result_frame, text="Copy", command=copy_result)
    copy_button.pack(side="left", padx=10)

    movie_label.pack()
    movie_entry.pack()
    movie_button.pack()

    random_label.pack()
    random_button.pack()
    result_label.pack()



btn1 = tk.Button(app,text='Choose movie randomly', command=randomapp).grid(row=3,column=3)

app.mainloop()