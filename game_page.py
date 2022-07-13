
import wx
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
# module for colours and graphics - including fonts
from colours_and_graphics import *
from board_class import *
import random as r
import settings_handler as sh

class Board_Canvas(object):
    def __init__(self,root,board_width):
        self.c = Canvas(root,bg=get_colour(0), bd=0, highlightthickness=0, height=board_width, width=board_width)
        self.images = []
        self.board_width = board_width
        self.chess_board = None
        self.root = root
        self.eval_text_value = StringVar()
        self.eval_text_value.set("0")
        self.eval_text = Label(self.root, textvariable=self.eval_text_value, bg=get_colour(0), fg=get_colour(1))
        self.eval_text.config(font =(get_font(), self.board_width//30))
        self.sets = ["classic", "rabisco", "tyke"]
        self.display_text()
    def display(self):
        for image in self.images:
            self.c.create_image(image[0],image[1],image=image[2])
        self.display_text()
        self.root.update_idletasks()
    def display_text(self):

        # button_font = font.Font(family=get_font(), size=13, weight="bold")
        # piece_set_button = Button(self.root, text="Piece Set", width=10, height=2, command=lambda: change_piece_set(self.chess_board))
        # piece_set_button.config(fg=get_colour(4), bg=get_colour(6), borderwidth=0)
        # piece_set_button['font'] = button_font
        # piece_set_button.pack(side=RIGHT, padx=self.board_width*0.02)

        if self.chess_board:
            self.eval_text_value.set(str(self.chess_board.eval))
        self.eval_text.grid(column=4, row=1, padx=self.board_width*0.08)

    def clear(self, what="all"):
        self.images = []
        self.c.delete(what)

def change_piece_set(chess_board, chosen_set="classic"):
    sets = ["classic", "rabisco", "tyke"]
    chess_board.piece_set = chosen_set
    chess_board.display_board()


def piece_set_callback(set_var, name, index, mode):
    global chess_board_global
    # print(f"piece set changed")
    change_piece_set(chess_board_global, set_var.get())

def stockfish_skill_callback(skill_var, name, index, mode):
    if skill_var == "easy":
        sf_skill_level(-20)
    elif skill_var == "medium":
        sf_skill_level(-5)
    elif skill_var == "hard":
        sf_skill_level(3)
    elif skill_var == "impossible":
        sf_skill_level(20)


def clicked(event, board_width, chess_board, c):
    ix = int(event.x//(board_width/8))
    iy = int(event.y//(board_width/8))
    index = ix + iy * 8

    if event.y < 30 or event.x > board_width or event.y > board_width:
        return

    if index in chess_board.current_valid_moves:
        perform_move(index, chess_board)


        # print(chess_board.eval)
    chess_board.current_valid_moves = []

    if chess_board.current_highlighted:
        chess_board.current_highlighted.highlighted = False

    chess_board.board[index].highlighted = True
    chess_board.current_highlighted = chess_board.board[index]

    pos_moves = []

    if chess_board.board[index].piece_on_top:
        pos_moves = chess_board.board[index].piece_on_top.current_allowed_moves

    # if chess_board.board[index].piece_on_top:
    #     for move in chess_board.board[index].piece_on_top.valid_moves(chess_board):
    #         if chess_board.check_if_move_valid(move,index,chess_board):
    #             pos_moves.append(move)
    chess_board.display_board(pos_moves)


chess_board_global = None
def create_game_gui(player_side=0,old_root=None):
    global chess_board_global
    if old_root:
        old_root.destroy()
    # create window
    board_width = 600
    root = Tk()
    root.title("Menu")
    app = wx.App(False)
    root.geometry(f"{int(board_width*1.2)}x{board_width+30}+{(wx.GetDisplaySize()[0]//2)-int(board_width*1.6/2)}+{(wx.GetDisplaySize()[1]//2)-int(board_width/2)}")
    root.configure(background=get_colour(0))
    root.resizable(False, False)

    sets = ["classic", "rabisco", "tyke"]
    set_var = StringVar(root)
    set_var.set(sets[0])
    opt = OptionMenu(root, set_var, *sets)
    opt.config(width=10, font=(get_font(), 12), bg=get_colour(4), borderwidth=0, fg=get_colour(1))
    opt.grid(column=0, row=0, sticky="w")

    skill_levels = ["easy", "medium", "hard", "impossible"]
    skill_var = StringVar(root)
    skill_var.set(skill_levels[1])
    opt_sk = OptionMenu(root, skill_var, *skill_levels)
    opt_sk.config(width=10, font=(get_font(), 12), bg=get_colour(4), borderwidth=0, fg=get_colour(1))
    opt_sk.grid(column=1, row=0, sticky="w")

    canv = Board_Canvas(root,board_width)
    canv.c.grid(columnspan=3, column=0, row=1)

    chess_board = create_board(canv,board_width,player_side)
    canv.chess_board = chess_board
    chess_board.display_board()

    chess_board_global = chess_board

    set_var.trace("w", lambda *args: piece_set_callback(set_var, *args))
    skill_var.trace("w", lambda *args: stockfish_skill_callback(skill_var, *args))

    root.bind('<Button-1>',lambda event,
        A=board_width,
        B=chess_board,
        C=canv: clicked(event,A,B,C)
    )

    root.mainloop()

def create_board(canv,board_width,side=0):
    global chess_board_global
    chess_board = Board(canv,board_width)
    chess_board.set_up(side)
    return chess_board


if __name__ == "__main__":
    create_game_gui(int(r.random()*2))
