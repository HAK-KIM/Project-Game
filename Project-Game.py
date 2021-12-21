import tkinter as tk;
from random import randrange
root = tk.Tk()
root.geometry("600x600")
fram = tk.Frame()
fram.master.title("PNC UI GAME")
canvas = tk.Canvas(fram)




canvas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()