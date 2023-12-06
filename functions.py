from tkinter import *
from tkinter import messagebox
counter = 0
plays = 0

def reset(win):
    win.destroy()

def click(event,win, frm):
    global counter
    if counter%2 == 0:
        x = Label(frm, text="X", font=("None",24,"bold"))
        frm.winfo_children()[0].destroy()
        frm.winfo_children()[0] = x
        x.pack(expand=True, fill="both")
        counter += 1
    else:
        o = Label(frm, text="O", font=("None",24,"bold"))
        frm.winfo_children()[0].destroy()
        frm.winfo_children()[0] = o
        o.pack(expand=True, fill="both")
        counter += 1
    win_handle(win)

def win_handle(win):
    global score1,score2,plays
    if frames[0].winfo_children()[0]["text"]=="X" and frames[1].winfo_children()[0]["text"]=="X" and frames[2].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[3].winfo_children()[0]["text"]=="X"  and frames[4].winfo_children()[0]["text"]=="X"  and frames[5].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[6].winfo_children()[0]["text"]=="X"  and frames[7].winfo_children()[0]["text"]=="X"  and frames[8].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[0].winfo_children()[0]["text"]=="X"  and frames[4].winfo_children()[0]["text"]=="X"  and frames[8].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[2].winfo_children()[0]["text"]=="X"  and frames[4].winfo_children()[0]["text"]=="X"  and frames[6].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[0].winfo_children()[0]["text"]=="X"  and frames[3].winfo_children()[0]["text"]=="X"  and frames[6].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[1].winfo_children()[0]["text"]=="X"  and frames[4].winfo_children()[0]["text"]=="X"  and frames[7].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)
    elif frames[2].winfo_children()[0]["text"]=="X"  and frames[5].winfo_children()[0]["text"]=="X"  and frames[8].winfo_children()[0]["text"] == "X":
        messagebox.showinfo(title="Winner", message="X wins!")
        reset(win=win)


    elif frames[0].winfo_children()[0]["text"]=="O"  and frames[1].winfo_children()[0]["text"]=="O"  and frames[2].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[3].winfo_children()[0]["text"]=="O"  and frames[4].winfo_children()[0]["text"]=="O"  and frames[5].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[6].winfo_children()[0]["text"]=="O"  and frames[7].winfo_children()[0]["text"]=="O"  and frames[8].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[0].winfo_children()[0]["text"]=="O"  and frames[4].winfo_children()[0]["text"]=="O"  and frames[8].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[0].winfo_children()[0]["text"]=="O"  and frames[3].winfo_children()[0]["text"]=="O"  and frames[6].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[1].winfo_children()[0]["text"]=="O"  and frames[4].winfo_children()[0]["text"]=="O"  and frames[7].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[2].winfo_children()[0]["text"]=="O"  and frames[5].winfo_children()[0]["text"]=="O"  and frames[8].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    elif frames[2].winfo_children()[0]["text"]=="O" and frames[4].winfo_children()[0]["text"]=="O" and frames[6].winfo_children()[0]["text"] == "O":
        messagebox.showinfo(title="Winner", message="O wins!")
        reset(win=win)
    for i in range(9):
        if frames[i].winfo_children()[0]["text"] != "":
            plays += 1
    if plays == 45:     #if all the frames arr full.
        messagebox.showinfo(title="No Winner", message="Equal")
        reset(win=win)


def game_board(win):
    global frames, default
    frames = []
    index = 0
    parent_frame = Frame(win)
    parent_frame.place(relx=0.5, rely=0.5, anchor="center")
    parent_frame.columnconfigure([0,1,2], weight=1)
    parent_frame.rowconfigure([0,1,2], weight=1)
    for row in range(3):
        for column in range(3):
            frm = Frame(parent_frame, highlightthickness=2, highlightbackground="black", width=100, height=100, background="lightgrey")
            frm.pack_propagate(False)  # prevents the frame to get small to fit the inner content
            frm.grid(row=row,column=column, sticky="nsew")
            default = Label(frm, text="", font=("None",24,"bold"))
            frames.append(frm)
            frm.bind("<Button-1>", lambda event, win=win, frame=frames[index]: click(event, win, frame))
            index +=1