


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
        [1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,1,3,1,9,1],
        [1,1,1,1,3,1,1,1,3,1,3,1,1,1,1,1,3,1,3,1],
        [2,0,0,0,0,0,9,1,0,1,3,1,3,0,3,0,3,1,3,1],
        [1,1,1,1,1,1,1,1,3,1,3,1,1,0,1,1,1,1,3,1],
        [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,3,3,1],
        [1,3,1,1,1,1,1,3,1,3,9,3,1,0,0,1,0,1,1,1],
        [1,3,3,3,9,0,1,3,1,1,1,1,1,0,1,1,0,1,3,1],
        [1,3,1,1,1,1,1,3,1,9,1,9,3,3,3,3,3,1,3,1],
        [1,3,1,9,3,3,3,3,3,3,1,3,1,1,3,1,1,1,3,1],
        [1,9,1,3,1,1,1,1,1,1,1,3,3,1,3,3,3,3,3,1],
        [1,0,1,3,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1],
        [1,1,1,3,1,3,1,1,1,1,1,1,3,1,3,3,3,3,3,1],
        [1,3,3,3,1,3,1,3,3,3,3,3,3,1,3,1,1,1,3,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,9,3,3,1,3,3,3,1],
        [1,3,1,3,9,3,1,3,1,1,1,1,1,1,1,1,1,1,3,1],
        [1,3,1,3,1,3,1,3,1,3,3,3,3,3,3,3,3,3,3,1],
        [1,3,1,3,1,3,3,9,3,1,6,3,3,1,1,1,1,1,1,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,3,3,3,9,3,3,9,1],
        [1,3,3,3,3,3,1,3,3,3,3,9,3,1,3,3,3,3,3,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
# variables--------------------------------
Hole = 6
Player = 2
Wall = 1
Door = 5
Bomb = 9
Coins = 3
WiningPlace = 6
PlayerLives = 3
Win = False
Lost = False
win_sound = False
Lost_sount = False
colect_sound = False
point = 0
# insert images---------------------------- 
wall=tk.PhotoImage(file='images\wallnew.png')
player=tk.PhotoImage(file='images\santa25.png')
maze =tk.PhotoImage(file='images\start game.png')
background =tk.PhotoImage(file='images\christmasBG.png')
hart =tk.PhotoImage(file='images\Heart27-re.png')
coins =tk.PhotoImage(file='images\dollar.png')
bomb =tk.PhotoImage(file='images\Bomb.png')
win=tk.PhotoImage(file='images\youwin.png')
lost=tk.PhotoImage(file='images\gameover.png')
Winnig=tk.PhotoImage(file='images\wining.png')
About=tk.PhotoImage(file='images\About-button.png')
mazegames=tk.PhotoImage(file='images\poster.png')
button=tk.PhotoImage(file='images\Btnlast-removebg.png')
back=tk.PhotoImage(file='images\Back100x70-removebg.png')
buttonPoint=tk.PhotoImage(file='images\ButtonPoint-removebg.png')
buttonheart=tk.PhotoImage(file='images\ButtonHeart-removebg.png')
# functions-------------------------------
# Graphic game
def arrayToDrawing():
    global point, grid, Win, Lost, PlayerLives
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
            elif grid[row][col]==6:
                canvas.create_image(156+col*25,87+row*25, image=Winnig)
    countPoints()
    playerlife()
    NextandBack()

# get index ot player
def getIndexof1(grid):
    indexOf1=0
    for row in range(len(grid)):
        sub=grid[row]
        for col in range(len(sub)):
            if sub[col]==2:
                indexOf1=[row, col]
    return indexOf1

# player lives
def playerlife():
    global PlayerLives, grid
    index=getIndexof1(grid)
    canvas.create_image( 180, 0,image=buttonheart, anchor = "nw")
    canvas.create_text(230, 40, text='',font=('Arial',20))
    for i in range(PlayerLives):
        canvas.create_image(250+40*i,20,image=hart,anchor='nw')
# count points
def countPoints():
    global grid, point, Coins
    index = getIndexof1(grid)
    canvas.create_image( 450, 8,image=buttonPoint, anchor = "nw")
    canvas.create_text(550,38, text=str(point), font=('Arial',20))
# display sounds
def clickSound():
    winsound.PlaySound('Sounds\click.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def gameSound():
    winsound.PlaySound('Sounds\musicgame.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def walkSound():
    winsound.PlaySound('Sounds\walk2.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def coinSound():
    winsound.PlaySound('Sounds\coin2.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
def bombSound():
    winsound.PlaySound('Sounds\Bomb', winsound.SND_FILENAME | winsound.SND_ASYNC)
def winningSound():
    winsound.PlaySound('Sounds\winning.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
# next and back button
def NextandBack():
    canvas.create_image( 18,-5, image =About, anchor = "nw" ,tags="back")
    canvas.create_text(65, 29, text = "BACK", fill="blue", font=("Roboto, 15 italic bold"), tags="back")
    canvas.create_image( 690, -5,  image =About, anchor = "nw" ,tags="about")
    canvas.create_text(738, 29, text = "ABOUT", fill="blue", font=("Roboto, 15 italic bold"), tags="about")

def about(event):
    canvas.create_rectangle(140,70,650,600,fill="white",tags='bgsenario')
    canvas.create_rectangle(620,80,640,100,fill="red",tags='remove')
    canvas.create_text(630,90,text="X" ,fill="white",font=("Arial",15),tags='remove')
    canvas.create_text(285, 190, font="Purisa",text="- Step1: Click start to play game", tags="senario")
    canvas.create_text(335, 220, font="Purisa",text="- Step2: Santa-claus find the way go to Black-Hole.", tags="senario")
    canvas.create_text(335, 250, font="Purisa",text="But have some Bomb on the way.", tags="senario")
    canvas.create_text(350, 280, font="Purisa",text="- Step3: If Santa-claus meet one Bomb it will lose 1 lift.", tags="senario")
    canvas.create_text(345, 310, font="Purisa",text="If Santa-claust lose 3 lift Game over!", tags="senario")
    canvas.create_text(390, 340, font="Purisa",text="- Step4: If Santa-claust arrive Black-Hole whit 500 coins it will Win.", tags="senario")
    canvas.create_text(405, 370, font="Purisa",text="But Santa-claust don't have enought coin cannot Win. ", tags="senario")
    canvas.create_text(205, 400, font="Purisa,",text="Note:", tags="senario")
    canvas.create_text(250, 430, font="Purisa",text="(A) = moveleft", tags="senario")
    canvas.create_text(255, 460, font="Purisa",text="(D) = moveright", tags="senario")
    canvas.create_text(250, 490, font="Purisa",text="(W) = moveup", tags="senario")
    canvas.create_text(257, 520, font="Purisa",text="(S) = movedown", tags="senario")

def remove(event):
    canvas.delete('remove')
    canvas.delete('bgsenario')
    canvas.delete('senario')
# dis play win or lost
def WinOrLost():
    global Win, Lost, grid, point
    if Win and point >=500:
        canvas.create_image( 0, 0, image = win, anchor = "nw")
        canvas.create_image( 690, -5,  image =About, anchor = "nw" ,tags="about")
        canvas.create_text(738, 29, text = "Replay", fill="blue", font=("Roboto, 15 italic bold"), tags="about")

    elif Win and point<500:
        canvas.create_rectangle(200, 280, 600, 320, fill="#ffffff",outline="", tags="next")
        canvas.create_text(400,300, text = 'Not enough point, play again!', font=('Arial', 20))
        canvas.create_image( 350, 310,  image =About, anchor = "nw" ,tags="about")
        canvas.create_text(400, 345, text = "Retry", fill="blue", font=("Roboto, 15 italic bold"), tags="back")

    elif Lost:
        canvas.create_image( 0, 0, image = lost, anchor = "nw")
        canvas.create_image( 18,-5, image =About, anchor = "nw" ,tags="back")
        canvas.create_text(65, 29, text = "Retry", fill="blue", font=("Roboto, 15 italic bold"), tags="back")
        canvas.create_image( 690, -5,  image =About, anchor = "nw" ,tags="about")
        canvas.create_text(738, 29, text = "ABOUT", fill="blue", font=("Roboto, 15 italic bold"), tags="about")

# moving space
def move(deltaX, deltaY):
    global Win, Lost, Coins, point, PlayerLives, walk_sound, colect_sound
    index=getIndexof1(grid)
    numberOfColumn = len(grid[0])
    if grid[index[0]+deltaY][index[1]+deltaX]==Coins:
        colect_sound = True
        if colect_sound:
            coinSound()
        elif grid[index[0]+deltaY][index[1]+deltaX]==player:
            colect_sound = False
            if walk_sound == True:
                walkSound()
        point +=5
    if grid[index[0]+deltaY][index[1]+deltaX]==Bomb:
        bombSound()
        PlayerLives -= 1
    if grid[index[0]+deltaY][index[1]+deltaX]==0:
        walkSound()
    if index[1]+deltaX < numberOfColumn and index[0]+deltaY <len(grid) and index[0]+deltaY>=0 and grid[index[0]+deltaY][index[1]+deltaX]!=Wall:
        grid[index[0]][index[1]]=0
        grid[index[0]+deltaY][index[1]+deltaX]=2
    arrayToDrawing()
    if grid[17][10]==2:
        winningSound()
        Win =True
        WinOrLost()
    elif PlayerLives ==0:
        walk_sound = False
        Lost = True
        WinOrLost()

# move right----------------------------------
def moveright(event):
    global Win, Lost, walk_sound, colect_sound
    if not Win and not Lost:
        move(1,0)

# # move left-----------------------------------
def moveleft(event):
    global Win, Lost, walk_sound, colect_sound
    if not Win and not Lost:
        move(-1, 0)

# move up-----------------------------------
def moveup(event):
    global Win, Lost, walk_sound, colect_sound
    if not Win and not Lost:
        move(0,-1)

# move down
def movedown(event):
    global Win, Lost, walk_sound, colect_sound
    if not Win and not Lost:
        move(0, 1)

# game interface
def game(event):
    arrayToDrawing()
    gameSound()
    
def start():
    canvas.create_image(0,0,image=maze,  anchor = 'nw')
    #Text Start
    canvas.create_image( 215, 405,image=button, anchor = "nw" ,tags="start")
    canvas.create_text(407, 445, text = "Start", fill="white", font="Times 45 bold", tags="start")
    #Text Exit
    canvas.create_image( 215, 485,image=button, anchor = "nw" ,tags="exit")
    canvas.create_text(405, 525, text = "Exit", fill="white", font="Times 45 bold", tags="exit")
    
# Begining of game
def begin():
    canvas.create_image(0,0,image=mazegames,  anchor = 'nw')
    canvas.after(2000, start)
begin()

# back and Exit
def Back(event):
    global grid, point, Win, Lost, PlayerLives
    start()
    PlayerLives = 3
    Win = False
    Lost = False
    point = 0
    grid=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,3,3,3,3,3,3,3,3,1,3,3,3,3,3,1,3,1,9,1],
        [1,1,1,1,3,1,1,1,3,1,3,1,1,1,1,1,3,1,3,1],
        [2,0,0,0,0,0,9,1,0,1,3,1,3,0,3,0,3,1,3,1],
        [1,1,1,1,1,1,1,1,3,1,3,1,1,0,1,1,1,1,3,1],
        [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,3,3,1],
        [1,3,1,1,1,1,1,3,1,3,9,3,1,0,0,1,0,1,1,1],
        [1,3,3,3,9,0,1,3,1,1,1,1,1,0,1,1,0,1,3,1],
        [1,3,1,1,1,1,1,3,1,9,1,9,3,3,3,3,3,1,3,1],
        [1,3,1,9,3,3,3,3,3,3,1,3,1,1,3,1,1,1,3,1],
        [1,9,1,3,1,1,1,1,1,1,1,3,3,1,3,3,3,3,3,1],
        [1,0,1,3,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1],
        [1,1,1,3,1,3,1,1,1,1,1,1,3,1,3,3,3,3,3,1],
        [1,3,3,3,1,3,1,3,3,3,3,3,3,1,3,1,1,1,3,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,9,3,3,1,3,3,3,1],
        [1,3,1,3,9,3,1,3,1,1,1,1,1,1,1,1,1,1,3,1],
        [1,3,1,3,1,3,1,3,1,3,3,3,3,3,3,3,3,3,3,1],
        [1,3,1,3,1,3,3,9,3,1,6,3,3,1,1,1,1,1,1,1],
        [1,3,1,3,1,3,1,3,1,1,1,1,3,3,3,9,3,3,9,1],
        [1,3,3,3,3,3,1,3,3,3,3,9,3,1,3,3,3,3,3,1],
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
canvas.tag_bind("about", "<Button-1>", about)
canvas.tag_bind("remove", "<Button-1>", remove)
canvas.tag_bind("tryagain", "<Button-1>",Back)

canvas.pack(expand=True, fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()


