from tkinter import *
from functions import *
width, height = 400,430
win = Tk()
win.minsize(width,height)
win.title("Tic Tac Toe Game")
win.configure(bg="lightblue")
win.iconbitmap("./xo.ico")


game_board(win)
win.mainloop()

