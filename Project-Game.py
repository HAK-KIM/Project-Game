


import tkinter as tk;
import random
import winsound
from random import randrange
from tkinter.constants import X, Y
root = tk.Tk()
root.geometry("800x650")
fram = tk.Frame()
fram.master.title("Maze Game")
root.resizable(0,0)
canvas =tk.Canvas(fram)
# grid display
grid=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,0,3,0,3,0,3,0,1,0,3,0,3,0,1,0,1,9,1],
        [1,1,1,1,0,1,1,1,3,1,0,1,1,1,1,1,0,1,0,1],
        [2,0,0,0,0,0,0,1,0,1,3,1,3,0,3,0,3,1,3,1],
        [1,1,1,1,1,1,1,1,3,1,0,1,1,0,1,1,1,1,0,1],
        [1,3,0,3,0,3,0,3,0,3,0,3,0,3,0,1,3,0,3,1],
        [1,0,1,1,1,1,1,0,1,3,9,3,1,0,0,1,0,1,1,1],
        [1,3,3,9,3,3,1,0,1,1,1,1,1,0,1,1,0,1,3,1],
        [1,0,1,1,1,1,1,0,1,9,1,9,3,0,3,0,3,1,0,1],
        [1,3,1,0,3,0,3,0,3,0,1,3,0,1,0,1,1,1,3,1],
        [1,9,1,3,1,1,1,1,1,1,1,3,1,1,0,3,0,3,0,1],
        [1,3,1,0,1,3,0,3,0,3,3,0,3,1,1,1,1,1,1,1],
        [1,1,1,3,1,0,1,1,1,1,1,1,0,1,0,3,0,3,0,1],
        [1,0,3,0,1,3,1,0,3,0,3,0,3,1,3,1,1,1,0,1],
        [1,3,1,3,1,0,1,3,1,1,1,1,0,9,0,1,0,0,3,1],
        [1,0,1,9,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,3,1,3,1,3,1,3,1,0,3,0,3,0,3,0,3,0,3,1],
        [1,0,1,0,1,0,9,0,0,1,6,0,9,1,1,1,1,1,1,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,0,3,0,3,0,3,0,1],
        [1,0,3,0,3,0,1,0,3,0,9,3,0,1,3,3,9,3,3,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
# variables--------------------------------
Player = 2
Wall = 1
Door = 5
Bomb = 9
Coins = 3
PlayerLives = 3
Win = False
Lost = False
win_sound = False
Lost_sount = False
point = 0
# insert images---------------------------- 
wall=tk.PhotoImage(file='wallnew.png')
player=tk.PhotoImage(file='santa25.png')
maze =tk.PhotoImage(file='start game.png')
background =tk.PhotoImage(file='christmasBG.png')
hart =tk.PhotoImage(file='hart32.png')
coins =tk.PhotoImage(file='dollar.png')
bomb =tk.PhotoImage(file='bomb.png')
win=tk.PhotoImage(file='youwin.png')

# functions-------------------------------
# drawing grid
def arrayToDrawing():
    global point, grid, Win, Lost
    index = getIndexof1(grid)
    canvas.delete('all')
    canvas.create_image(0,0,image=background,anchor='nw')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1:
                canvas.create_image(170+col*25,100+row*25, image=wall, anchor = 'se')
            elif grid[row][col]==Player and grid[row][col]!=Wall:
                canvas.create_image(158+col*25,88+row*25, image=player)
            elif grid[row][col]==Coins:
                canvas.create_image(160+col*25,89+row*25, image=coins)
            elif grid[row][col]==Bomb:
                canvas.create_image(160+col*25,89+row*25, image=bomb)
    canvas.create_rectangle(450, 8, 590, 50, fill="white",outline="")
    canvas.create_text(520,30, text='Point : '+str(point), font=('Arial',20))
    if grid[index[0]][index[1]+1]==3 or grid[index[0]][index[1]-1]==3 or grid[index[0]+1][index[1]]==3 or grid[index[0]-1][index[1]]==3:
        point +=5
    canvas.create_rectangle(180, 8, 410, 50, fill="white",outline="")
    canvas.create_text(230, 30, text='Lives: ',font=('Arial',20))
    canvas.create_rectangle(18, 8, 85, 35, fill="#eeeeee",outline="", tags="back")
    canvas.create_text(50, 20, text = "<Back", fill="blue", font=("Arial",15), tags="back")
    canvas.create_rectangle(710, 8, 780, 35, fill="#eeeeee",outline="", tags="next")
    canvas.create_text(740, 20, text = "Next>", fill="blue", font=("Arial",15), tags="next")
    for i in range(PlayerLives):
        canvas.create_image(280+40*i,13,image=hart,anchor='nw')
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
    global Win, Lost, Coins, point
    index=getIndexof1(grid)
    numberOfColumn = len(grid[0])
    if index[1]+deltaX < numberOfColumn and index[0]+deltaY <len(grid) and index[0]+deltaY>=0 and grid[index[0]+deltaY][index[1]+deltaX]!=Wall:
        grid[index[0]][index[1]]=0
        grid[index[0]+deltaY][index[1]+deltaX]=2
    arrayToDrawing()
    if grid[17][10]==2:
        Win =True
        WinOrLost()
# dis play win or lost
def WinOrLost():
    global Win, Lost
    if Win:
        canvas.create_image( 0, 0, image = win, anchor = "nw")
        canvas.create_rectangle(710, 8, 780, 35, fill="#eeeeee",outline="", tags="next")
        canvas.create_text(740, 20, text = "Next>", fill="blue", font=("Arial",15), tags="next")
    if Lost:
        canvas.create_image( 0, 0, image = win, anchor = "nw")
        canvas.create_rectangle(18, 8, 85, 35, fill="#eeeeee",outline="", tags="back")
        canvas.create_text(50, 20, text = "<Back", fill="blue", font=("Arial",15), tags="back")
# move right----------------------------------
def moveright(event):
    global Win
    if not Win:
        move(1,0)
        winsound.PlaySound('Sounds\click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
# move left-----------------------------------
def moveleft(event):
    global Win
    if not Win:
        move(-1, 0)
        winsound.PlaySound('Sounds\click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
# move up-----------------------------------
def moveup(event):
    global Win
    if not Win:
        move(0,-1)
        winsound.PlaySound('Sounds\click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
# move down
def movedown(event):
    global Win
    if not Win:
        move(0, 1)
        winsound.PlaySound('Sounds\click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
# game interface
def game(event):
    winsound.PlaySound('Sounds\music-game.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    arrayToDrawing()
    
# start game
def start():
    winsound.PlaySound('Sounds\music-game.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(0,0,image=maze,  anchor = 'nw')
    #Text Start
    canvas.create_rectangle(230, 420, 575, 490, fill="#eeeeee",outline="", tags="start")
    canvas.create_text(410, 453, text = "Start", fill="#ff9800", font="Times 45 italic bold", tags="start")
    #Text Exit
    canvas.create_rectangle(230, 500, 575, 570, fill="#eeeeee",outline="", tags="exit")
    canvas.create_text(400, 533, text = "Exit", fill="#ff9800", font="Times 45 italic bold", tags="exit")
    
# Begining of game
def begin():
    canvas.create_text(380, 360, text = "Loading...", fill="black", font="Times 20 italic bold", tags="welcome")
    canvas.after(2000, start)
begin()
# back and Exit

def Back(event):
    global grid, point
    start()
    point = 0
    grid=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,0,3,0,3,0,3,0,1,0,3,0,3,0,1,0,1,9,1],
        [1,1,1,1,0,1,1,1,3,1,0,1,1,1,1,1,0,1,0,1],
        [2,0,0,0,0,0,0,1,0,1,3,1,3,0,3,0,3,1,3,1],
        [1,1,1,1,1,1,1,1,3,1,0,1,1,0,1,1,1,1,0,1],
        [1,3,0,3,0,3,0,3,0,3,0,3,0,3,0,1,3,0,3,1],
        [1,0,1,1,1,1,1,0,1,3,9,3,1,0,0,1,0,1,1,1],
        [1,3,3,9,3,3,1,0,1,1,1,1,1,0,1,1,0,1,3,1],
        [1,0,1,1,1,1,1,0,1,9,1,9,3,0,3,0,3,1,0,1],
        [1,3,1,0,3,0,3,0,3,0,1,3,0,1,0,1,1,1,3,1],
        [1,9,1,3,1,1,1,1,1,1,1,3,1,1,0,3,0,3,0,1],
        [1,3,1,0,1,3,0,3,0,3,3,0,3,1,1,1,1,1,1,1],
        [1,1,1,3,1,0,1,1,1,1,1,1,0,1,0,3,0,3,0,1],
        [1,0,3,0,1,3,1,0,3,0,3,0,3,1,3,1,1,1,0,1],
        [1,3,1,3,1,0,1,3,1,1,1,1,0,9,0,1,0,0,3,1],
        [1,0,1,9,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,3,1,3,1,3,1,3,1,0,3,0,3,0,3,0,3,0,3,5],
        [1,0,1,0,1,0,9,0,1,0,3,0,9,1,1,1,1,1,1,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,0,3,0,3,0,3,0,1],
        [1,0,3,0,3,0,1,0,3,0,9,3,0,1,3,3,9,3,3,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
def Exit(event):
   root.quit()

root.bind('<w>',moveup)
root.bind('<s>', movedown)
root.bind('<a>', moveleft)
root.bind('<d>', moveright)

canvas.tag_bind("start", "<Button-1>", game)
canvas.tag_bind("exit", "<Button-1>", Exit)
canvas.tag_bind("back", "<Button-1>", Back)
canvas.tag_bind("next", "<Button-1>", Back)

canvas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()


