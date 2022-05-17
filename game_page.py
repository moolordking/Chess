
import wx
from tkinter import *
from PIL import Image, ImageTk
# module for colours and graphics - including fonts
from colours_and_graphics import *
from board_class import *

def get_all_moves_from_side(side,chess_board):
    arr = []
    for side_square in chess_board.board:
        if side_square.piece_on_top and side_square.piece_on_top.col == side:
            arr.append(side_square.piece_on_top.valid_moves(chess_board))
    return arr

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
        self.display_text()
    def display(self):
        for image in self.images:
            self.c.create_image(image[0],image[1],image=image[2])
        self.display_text()
    def display_text(self):
        if self.chess_board:
            self.eval_text_value.set(str(self.chess_board.eval))
        self.eval_text.pack(side=RIGHT, padx=self.board_width*0.25)

    def clear(self, what="all"):
        self.images = []
        self.c.delete(what)

def clicked(event, board_width, chess_board, c):
    ix = int(event.x//(board_width/8))
    iy = int(event.y//(board_width/8))
    index = ix + iy * 8

    if index in chess_board.current_valid_moves:
        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index])
        chess_board.calculate_current_side_moves()
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
    #         if check_if_move_valid(move,index,chess_board):
    #             pos_moves.append(move)
    chess_board.display_board(pos_moves)

def create_game_gui(player_side=0,old_root=None):
    if old_root:
        old_root.destroy()
    # create window
    board_width = 600
    root = Tk()
    root.title("Menu")
    app = wx.App(False)
    root.geometry(f"{int(board_width*1.6)}x{board_width}+{(wx.GetDisplaySize()[0]//2)-int(board_width*1.6/2)}+{(wx.GetDisplaySize()[1]//2)-int(board_width/2)}")
    root.configure(background=get_colour(0))
    root.resizable(False, False)

    canv = Board_Canvas(root,board_width)
    canv.c.pack(anchor='w')

    chess_board = create_board(canv,board_width,player_side)
    canv.chess_board = chess_board
    chess_board.display_board()

    root.bind('<Button-1>',lambda event,
        A=board_width,
        B=chess_board,
        C=canv: clicked(event,A,B,C)
    )

    root.mainloop()

def create_board(canv,board_width,side=0):
    chess_board = Board(canv,board_width)
    chess_board.set_up(side)
    return chess_board


if __name__ == "__main__":
    create_game_gui()