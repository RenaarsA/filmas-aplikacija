import tkinter as tk
from tkinter import Label

logs = tk.Tk()

logs.title('Filmu ģenerātors')
logs.eval('tk::PlaceWindow . center')  
logs.geometry('350x150') 
label = Label(logs) 


filma = tk.Label(logs,text='Filmas Nosaukums')
filma.grid(row=1,column=3)

filmaslogs = tk.Entry(logs)
filmaslogs.grid(row=1,column=2)




logs.mainloop()