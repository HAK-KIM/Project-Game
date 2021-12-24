


import tkinter as tk;
import random
import winsound
from random import randrange
from tkinter.constants import X, Y
root = tk.Tk()
root.geometry("800x650")
fram = tk.Frame()
fram.master.title("Maze Game")
canvas =tk.Canvas(fram)
# grid display
grid=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
        [1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
        [2,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1],
        [1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1],
        [1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
# variables--------------------------------
Up = False
Down = False
Left = False
Right = False
Win = False
Lost = False
# insert images---------------------------- 
wall=tk.PhotoImage(file='wallnew.png')
player=tk.PhotoImage(file='sata.png')
door =tk.PhotoImage(file='door32.png')
maze =tk.PhotoImage(file='start game.png')
background =tk.PhotoImage(file='christmasBG.png')

def game(event):
    arrayToDrawing()

def start():
    canvas.create_image(0,0,image=maze,  anchor = 'nw')
    #Text Start
    canvas.create_rectangle(230, 420, 575, 490, fill="#eeeeee",outline="", tags="start")
    canvas.create_text(410, 453, text = "Start", fill="#ff9800", font="Times 45 italic bold", tags="start")

    #Text Exit
    canvas.create_rectangle(230, 500, 575, 570, fill="#eeeeee",outline="", tags="exit")
    canvas.create_text(400, 533, text = "Exit", fill="#ff9800", font="Times 45 italic bold", tags="exit")
    

def begin():
    canvas.create_text(380, 360, text = "Loading...", fill="black", font="Times 20 italic bold", tags="welcome")
    canvas.after(2000, start)
begin()
def Back(event):
    start()
def Exit(event):
   root.quit()


# functions-------------------------------
# drawing grid
def arrayToDrawing():
    canvas.delete('all')
    canvas.create_image(0,0,image=background,anchor='nw')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1:
                canvas.create_image(170+col*25,100+row*25, image=wall, anchor = 'se')
                # canvas.create_rectangle(170+col*25,100+row*25,col*25,125+row*25,fill='blue')
            elif grid[row][col]==2 and grid[row][col]!=1:
                canvas.create_image(160,160, image=player)
    canvas.create_text(50, 20, text = "<Back", fill="black", font=("Arial",15), tags="back")

# display win
def iswin():
    canvas.create_image(300,350, image=winner)
    
# get index ot player
def getIndexof1(grid):
    indexOf1=0
    for row in range(len(grid)):
        sub=grid[row]
        for col in range(len(sub)):
            if sub[col]==2:
                indexOf1=[row, col]
    return indexOf1
# moving of player
def move(deltaX, deltaY):
    index1=getIndexof1(grid)
    numberOfColumn = len(grid[0])
    if deltaX == 1 and deltaY==0:
        if index1[1]+1 < numberOfColumn and grid[index1[0]][index1[1]+1]!=1:
            grid[index1[0]][index1[1]]=0
            grid[index1[0]][index1[1]+1]=2
        if grid[16][19]==2:
           iswin()
    elif deltaX == -1 and deltaY==0:
        if index1[1]-1 >=0 and grid[index1[0]][index1[1]-1]!=1: 
            grid[index1[0]][index1[1]]=0
            grid[index1[0]][index1[1]-1]=2
        if grid[16][19]==2:
           iswin()
    elif deltaX==0 and deltaY==-1:
        if index1[0]-1 <len(grid) and index1[0]-1>=0 and grid[index1[0]-1][index1[1]]!=1:
            grid[index1[0]][index1[1]]=0
            grid[index1[0]-1][index1[1]]=2
    elif deltaX == 0 and deltaY == 1:
        if index1[0]+1 <len(grid) and grid[index1[0]+1][index1[1]]!=1:
            grid[index1[0]][index1[1]]=0
            grid[index1[0]+1][index1[1]]=2
    arrayToDrawing()
    
def moveright(event):
    move(1,0)

def moveleft(event):
    move(-1, 0)

def moveup(event):
    move(0,-1)

def movedown(event):
    move(0, 1)

root.bind('<w>',moveup)
root.bind('<s>', movedown)
root.bind('<a>', moveleft)
root.bind('<d>', movedown)

canvas.tag_bind("start", "<Button-1>", game)
canvas.tag_bind("exit", "<Button-1>", Exit)
canvas.tag_bind("back", "<Button-1>", Back)

canvas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()


