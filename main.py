import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import stockfish
from stockfish import Stockfish

stockfish = Stockfish('stockfish_20011801_x64.exe')

root = tk.Tk()
root.title("Chess Analysis")
root.resizable(0, 0)
root.iconphoto(False, PhotoImage(file='favicon.png'))
ft = tkFont.Font(family='Times',size=10)

moves = []

def start():
    sbutton.config(text='    Reset    ', command=reset)
    move.config(state=ACTIVE)
    movetext.config(state=NORMAL)

def reset():
    root.quit()

def move():
    global moves
    m = movetext.get(1.0,4.0).strip("\n")
    moves.append(m)
    stockfish.set_position(moves)
    movetext.delete('1.0', END)
    movetext.insert('1.0', stockfish.get_best_move())
    bestm.config(state=NORMAL)
    bestm.delete('1.0',END)
    bestm.insert(1.0,"Best Move: " + stockfish.get_best_move())
    bestm.config(state=DISABLED)
    board.config(state=NORMAL)
    board.delete('1.0',END)
    board.insert(1.0,stockfish.get_board_visual())
    board.config(state=DISABLED)

sbutton = Button(text='    Start    ', command=start)
sbutton.grid(row=0,column=0,padx=0,pady=3)

move = Button(text=' Enter Move ', command=move,state=DISABLED)
move.grid(row=0,column=1,padx=3)

movetext = Text(height=1, width=10)
movetext.grid(row=0,column=2,padx=3,)
movetext.insert(1.0,"e2e4")
movetext.config(state=DISABLED)

board = Text(height=17, width=33)
board.grid(row=1,column=0,columnspan=3,padx=3, pady=0)
board.insert(1.0,stockfish.get_board_visual())
board.config(state=DISABLED)

bestm = Text(height=1, width=30)
bestm.grid(row=2,column=0,columnspan=3,padx=3, pady=3)
bestm.insert(1.0,"Best Move: " + stockfish.get_best_move())
bestm.config(state=DISABLED)

root.mainloop()