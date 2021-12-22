


import tkinter as tk;
import random
from random import randrange
from tkinter.constants import X, Y
root = tk.Tk()
root.geometry("800x800")
fram = tk.Frame()
fram.master.title("From Array to Graphics-step-1")
canvas =tk.Canvas(fram)

grid=[
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0,0],
        [0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0],
        [0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0],
        [0,2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,0,0,0,2,0,0,2,0],
        [0,0,0,0,0,2,0,2,0,0,0,2,0,2,0,2,2,2,2,2,0,0,2,0],
        [0,0,0,0,0,2,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0],
        [0,0,0,0,0,2,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0],
        [0,2,2,2,2,0,0,2,0,0,0,2,0,2,0,2,0,0,0,2,0,0,2,0],
        [0,2,0,0,2,0,0,2,2,2,2,2,0,0,0,2,0,0,0,2,2,2,2,0],
        [0,2,0,0,2,2,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0],
        [0,2,0,0,2,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0],
        [0,2,0,0,2,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0],
        [0,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
        [0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
        [0,2,0,0,0,2,0,0,0,0,0,2,0,0,2,2,2,2,2,2,0,0,0,0],
        [0,2,0,0,0,2,2,2,2,2,2,2,0,0,2,0,0,0,0,2,0,0,0,0],
        [0,2,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0],
        [0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0],
        [0,2,2,2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,5],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
mario=tk.PhotoImage(file='mario2.png')  
wall=tk.PhotoImage(file='wall32.png')
door =tk.PhotoImage(file='door32.png')
def arrayToDrawing():
    canvas.delete('all')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==0:
                canvas.create_image(30+col*30,30+row*30, image=wall, anchor = 'se')
            elif grid[row][col]==1 and grid[row][col]!=0:
                canvas.create_rectangle(col*30,row*30,30+col*30,30+row*30,fill="blue")
               #  canvas.create_image(col*30,row*30, image=mario)
            elif grid[row][col]==2:
                canvas.create_rectangle(col*30,row*30,30+col*30,30+row*30,fill="gray", outline= "")
            elif grid[row][col]==5:
               canvas.create_image(30+col*30,30+row*30, image=door, anchor = 'se')
arrayToDrawing()
# must be n, ne, e, se, s, sw, w, nw, or center
def getIndexof1(grid):
    indexOf1=0
    for row in range(len(grid)):
        sub=grid[row]
        for col in range(len(sub)):
            if sub[col]==1:
                indexOf1=[row, col]

    return indexOf1
print(getIndexof1(grid))
def WinOrLost():
   for row in range(len(grid)):
      for col in range(len(grid[row])):
         if grid[row][col]==5:
            


def moveright(event):
    # global grid
   index1=getIndexof1(grid)
   numberOfColumn = len(grid[0])
   if index1[1]+1 < numberOfColumn and grid[index1[0]][index1[1]+1]!=0:
      grid[index1[0]][index1[1]]=2
      grid[index1[0]][index1[1]+1]=1
   arrayToDrawing()



def moveleft(event):
    # global grid
    index1=getIndexof1(grid)
    if index1[1]-1 >=0 and grid[index1[0]][index1[1]-1]!=0: 
        grid[index1[0]][index1[1]]=2
        grid[index1[0]][index1[1]-1]=1
    arrayToDrawing()

def moveup(event):
    # global grid
    index1=getIndexof1(grid)
    if index1[0]-1 <len(grid) and index1[0]-1>=0 and grid[index1[0]-1][index1[1]]!=0:
        grid[index1[0]][index1[1]]=2
        grid[index1[0]-1][index1[1]]=1
    arrayToDrawing()


def movedown(event):
    # global grid
    index1=getIndexof1(grid)
    if index1[0]+1 <len(grid) and grid[index1[0]+1][index1[1]]!=0:
        grid[index1[0]][index1[1]]=2
        grid[index1[0]+1][index1[1]]=1
    arrayToDrawing()
root.bind("<a>",moveleft)
root.bind("<d>",moveright)
root.bind("<w>",moveup)
root.bind("<s>",movedown)

canvas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()


