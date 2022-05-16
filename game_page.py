
from tkinter import *
from PIL import Image, ImageTk
# module for colours and graphics - including fonts
from colours_and_graphics import *
from board_class import *

class Board_Canvas(object):
    def __init__(self,root,board_width):
        self.c = Canvas(root,bg=get_colour(0), bd=0, highlightthickness=0, height=board_width, width=board_width)
        self.images = []
        self.board_width = board_width
        self.chess_board = None
        self.root = root
        self.text = StringVar()
        self.text.set("0")
        self.eval_text = Label(self.root, textvariable=self.text, bg=get_colour(0), fg=get_colour(1))
        self.eval_text.config(font =(get_font(), self.board_width//30))
        self.display_text()
    def display(self):
        for image in self.images:
            self.c.create_image(image[0],image[1],image=image[2])
        self.display_text()
    def display_text(self):
        if self.chess_board:
            self.text.set(str(self.chess_board.eval))
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
        print(chess_board.eval)
    chess_board.current_valid_moves = []

    if chess_board.current_highlighted:
        chess_board.current_highlighted.highlighted = False

    chess_board.board[index].highlighted = True
    chess_board.current_highlighted = chess_board.board[index]

    pos_moves = []

    if chess_board.board[index].piece_on_top:
        for move in chess_board.board[index].piece_on_top.valid_moves(chess_board):
            king_can_be_taken = False

            for enemy_square in chess_board.board:
                if enemy_square.piece_on_top and enemy_square.piece_on_top.col != chess_board.board[index]:
                    temp_board = Board()
                    for i,square in enumerate(chess_board.board):
                        if square.piece_on_top:
                            if square.piece_on_top.piece_type.lower() == "pawn":
                                temp_board.board[i].add_piece(Pawn(square.piece_on_top.col))
                            if square.piece_on_top.piece_type.lower() == "rook":
                                temp_board.board[i].add_piece(Rook(square.piece_on_top.col))
                            if square.piece_on_top.piece_type.lower() == "knight":
                                temp_board.board[i].add_piece(Knight(square.piece_on_top.col))
                            if square.piece_on_top.piece_type.lower() == "queen":
                                temp_board.board[i].add_piece(Queen(square.piece_on_top.col))
                            if square.piece_on_top.piece_type.lower() == "king":
                                temp_board.board[i].add_piece(King(square.piece_on_top.col))
                            if square.piece_on_top.piece_type.lower() == "bishop":
                                temp_board.board[i].add_piece(Bishop(square.piece_on_top.col))
                    temp_board.move_piece(temp_board.board[index], temp_board.board[move])
                    for i,square in enumerate(temp_board.board):
                        if square.piece_on_top and square.piece_on_top.piece_type.lower() == "king" and square.piece_on_top.col == chess_board.board[index].piece_on_top.col:
                            king_location = i
                    for enemy_move in enemy_square.piece_on_top.valid_moves(temp_board):
                        temp_board.evaluate_position()
                        if enemy_move == king_location and (temp_board.eval>500 or temp_board.eval<500) and temp_board.board[enemy_square.position].piece_on_top.col != chess_board.board[index].piece_on_top.col:
                            king_can_be_taken = True
                            break
                    if king_can_be_taken:
                        break
            if not(king_can_be_taken):
                pos_moves.append(move)
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
    # chess_board.board[35].add_piece(Queen(0))
    return chess_board


if __name__ == "__main__":
    create_game_gui()