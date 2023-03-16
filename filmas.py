import random
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import webbrowser
from cgitb import text
from tkinter import Button, Entry, Label, Toplevel
import pyperclip
from tkinter import *

#tk loga izveide
app = tk.Tk()
app.title('Movie app')
app.eval('tk::PlaceWindow . center')
app.geometry('240x100')
label = Label(app)


#meklēšanas funkcija

def app1():
    def search_movie(): #meklē filmu, funkcija
        video_name = movie_entry.get() #iegūst datus no ievadītā logā
        query = video_name + " site:soap2day.id" #meklē nosukumu kopā ar saiti
        webbrowser.open(f"https://www.google.com/search?q={query}") #atver chrome un meklē query

    
    def search_anime(): #meklē anime, funkcija
        anime_name = anime_entry.get() #iegūst datus no ievadītā logā
        query = anime_name + " site:9anime.to" #meklē nosukumu kopā ar saiti
        webbrowser.open(f"https://www.google.com/search?q={query}") #atver chrome un meklē query

#izveido jaunu logu

    app = tk.Tk()
    app.title("Movie Search")
    app.geometry('320x60')
    

    movie_label = tk.Label(app,text="Enter movie name:").grid(row=1,column=2) #filmas loga nosaukums
    anime_label= tk.Label(app,text="Enter anime name:").grid(row=2,column=2) #anime loga nosaukums

    
    movie_entry = tk.Entry(app) #filmas loga ievade
    movie_entry.grid(row=1,column=3) #filmas loga atrašanās vieta

    anime_entry = tk.Entry(app) #anime loga ievade
    anime_entry.grid(row=2,column=3) #anime loga atrašanās vieta

    search_button_movie = tk.Button(app,text="Search Movie", command=search_movie).grid(row=1,column=4) #poga kuru uzpiežot darbojās filmas meklēšanas funkcija
    search_button_anime = tk.Button(app,text="Search Anime", command=search_anime).grid(row=2,column=4) #poga kuru uzpiežot darbojās anime meklēšanas funkcija



btn = tk.Button(app,text='Search Movie', command=app1) #poga ar kuru atverās jauns logs kurā atrodās meklēšanas funckija
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
#funkcija nejaušu datu izvēle no text faila

def randomapp(): 
    def save_to_file(): #datu saglabāšanas funkcija
        text = movie_entry.get() #iegūst datus no ievad loga
        with open("movies.txt", "a") as f: #izveido txt failu un atver to
            f.write(text + "\n") #ievadītais teksts saglababājās
        movie_entry.delete(0, tk.END)

    def choose_random_movie(): #funckija nejaušu datu ieguvei
        with open("movies.txt") as f: #atver izveidoto teksta failu
            movies = f.read().splitlines()
        if movies:
            chosen_movie = random.choice(movies) #ja ir dati teksta failā tad no tā teksta faila izvēls 1 nejaušu nosaukumu
            result_label.config(text=f"{chosen_movie}") #izvade
        else:
            result_label.config(text="No movies in the list yet!") #ja teksta failā nav ievadīti dati tad izvada, ka filmu nav
    
    def copy_result(): #kopēšanas funkcija
        result_text = result_label.cget("text") #pēc nejaušas izvades iegūst šo izvēlēto filmu
        pyperclip.copy(result_text) #kopē rezūlātu
    
#izveido jaunu logu

    root = tk.Tk()
    root.title("Movie Generator")
    root.geometry('400x150')

    movie_label = tk.Label(root, text="Enter a movie:") #
    movie_entry = tk.Entry(root) #filmas ievades logs
    movie_button = tk.Button(root, text="Add to list", command=save_to_file) #poga ar kuru saglabā loga ievadīto txt failā

    random_label = tk.Label(root, text="Click to choose a random movie:") #nejaušas izvēles loga nosaukums
    random_button = tk.Button(root, text="Random", command=choose_random_movie) #poga, nejaušas funkcijas darbībai

    
    result_frame = tk.Frame(root)
    result_frame.pack(side="bottom")

    
    result_label = tk.Label(result_frame, text="")
    result_label.pack(side="left")

    copy_button = tk.Button(result_frame, text="Copy", command=copy_result).pack(side="bottom", padx=10) #poga ar kopēšanas funkciju
    

    movie_label.pack()
    movie_entry.pack()
    movie_button.pack()

    random_label.pack()
    random_button.pack()
    result_label.pack()



btn1 = tk.Button(app,text='Movie Generator', command=randomapp) #poga ar kuru atverās jauns logs kurā atrodās nejaušas izvēles funckija
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
app.mainloop()