
from tkinter import *
from PIL import Image, ImageTk
# module for colours and graphics - including fonts
from colours_and_graphics import *
from board_class import *

class Board_Canvas(object):
    def __init__(self,root,board_width):
        self.c = Canvas(root,bg=get_colour(3), bd=0, highlightthickness=0, height=board_width, width=board_width)
        self.images = []
    def display(self):
        for image in self.images:
            self.c.create_image(image[0],image[1],image=image[2])
    def clear(self, what="all"):
        self.images = []
        self.c.delete(what)

def clicked(event, board_width, chess_board, c):
    ix = int(event.x//(board_width/8))
    iy = int(event.y//(board_width/8))
    index = ix + iy * 8

    if index in chess_board.current_valid_moves:
        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index])
        print(chess_board.eval)
    chess_board.current_valid_moves = []

    if chess_board.current_highlighted:
        chess_board.current_highlighted.highlighted = False

    chess_board.board[index].highlighted = True
    chess_board.current_highlighted = chess_board.board[index]
    pos_moves = []

    if chess_board.board[index].piece_on_top:
        pos_moves = chess_board.board[index].piece_on_top.valid_moves(chess_board)
    chess_board.display_board(pos_moves)

def create_game_gui(old_root=None):
    if old_root:
        old_root.destroy()
    # create window
    board_width = 500
    root = Tk()
    root.title("Menu")
    root.geometry(f"{int(board_width*1.6)}x{board_width}+{1080-board_width}+200")
    root.configure(background=get_colour(0))
    canv = Board_Canvas(root,board_width)
    canv.c.pack(anchor='w')

    chess_board = create_board(canv,board_width)
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
    # chess_board.board[35].add_piece(Queen(0))
    return chess_board


if __name__ == "__main__":
    create_game_gui()