
from square_class import *
from colours_and_graphics import *
from PIL import Image, ImageTk
import random as r
from show_messages import *

def check_for_checkmate(chess_board):
    for square in range(64):
        if chess_board.board[square].piece_on_top and chess_board.board[square].piece_on_top.col == chess_board.current_side:
            if len(chess_board.board[square].piece_on_top.current_allowed_moves)>0:
                return False
    return True

def perform_move(index, chess_board):
    # castling checks
    if chess_board.current_highlighted.piece_on_top.piece_type.lower() == "king" and (
            index == chess_board.current_highlighted.position + 2 or index == chess_board.current_highlighted.position - 2):
        if index == chess_board.current_highlighted.position + 2:
            if check_if_move_valid(index - 1, index - 2, chess_board):
                if not (chess_board.current_highlighted.piece_on_top.moved):
                    if chess_board.board[index + 1].piece_on_top and chess_board.board[
                        index + 1].piece_on_top.piece_type.lower() == "rook" and not (
                    chess_board.board[index + 1].piece_on_top.moved):
                        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index], "o-o")
                        chess_board.move_piece(chess_board.board[index + 1], chess_board.board[index - 1])
                    elif chess_board.board[index + 2].piece_on_top.piece_type.lower() == "rook" and not (
                    chess_board.board[index + 2].piece_on_top.moved):
                        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index], "o-o-o")
                        chess_board.move_piece(chess_board.board[index + 2], chess_board.board[index - 1])
        elif index == chess_board.current_highlighted.position - 2:
            if check_if_move_valid(index + 1, index + 2, chess_board):
                if not (chess_board.current_highlighted.piece_on_top.moved):
                    if chess_board.board[index - 1].piece_on_top and chess_board.board[
                        index - 1].piece_on_top.piece_type.lower() == "rook" and not (
                    chess_board.board[index - 1].piece_on_top.moved):
                        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index], "o-o")
                        chess_board.move_piece(chess_board.board[index - 1], chess_board.board[index + 1])
                    elif chess_board.board[index - 2].piece_on_top.piece_type.lower() == "rook" and not (
                    chess_board.board[index - 2].piece_on_top.moved):
                        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index], "o-o-o")
                        chess_board.move_piece(chess_board.board[index - 2], chess_board.board[index + 1])
    else:
        chess_board.move_piece(chess_board.current_highlighted, chess_board.board[index])

    chess_board.calculate_current_side_moves()

    # check if checkmate
    checkmate = check_for_checkmate(chess_board)
    if checkmate:
        winner = "white"
        if chess_board.current_side == 0: winner = "black"
        s_message(f"{winner} wins", "checkmate", 2)
        chess_board.current_side = 2

    print(chess_board.moves[len(chess_board.moves) - 1])

def get_all_moves_from_side(side,chess_board, check_for_empty=False, get_index_of_pieces=False):
    arr = []
    for side_square in chess_board.board:
        if side_square.piece_on_top and side_square.piece_on_top.col == side:
            if not(get_index_of_pieces):
                for move in side_square.piece_on_top.valid_moves(chess_board):
                    if check_if_move_valid(move,side_square.position,chess_board):
                        if check_for_empty:
                            return False
                        arr.append(move)
            else:
                if len(side_square.piece_on_top.valid_moves(chess_board))>0:
                    arr.append(side_square)
    return arr

def check_if_move_valid(move, index, chess_board):
    king_can_be_taken = False

    for enemy_square in chess_board.board:
        if enemy_square.piece_on_top and enemy_square.piece_on_top.col != chess_board.board[index].piece_on_top.col:
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
        return True

class Board(object):
    def __init__(self, canv=None, board_width=500):
        self.piece_set = "classic"
        self.board = [None] * 64
        self.current_side = 0
        self.player_side = 0
        self.current_highlighted = None
        self.board_width = board_width
        self.canv = canv
        self.current_valid_moves = []
        self.eval = 0
        self.currently_in_check = False
        self.moves = []
        self.next_move_dont_add = False
        for index in range(64):
            self.board[index] = Square(index, ((index+(index//8))%2!=0)*1)

        self.calculate_current_side_moves()

    def console_log_board(self):
        for j in range(8):
            current_pieces = ""
            for i in range(8):
                if self.board[(i+j*8)].piece_on_top != None:
                    square_piece = self.board[(i+j*8)].piece_on_top.piece_type
                    if square_piece.lower() == "knight":
                        square_piece = self.board[(i+j*8)].piece_on_top.piece_type[1::]
                    current_pieces += "["+square_piece[0]+"]"
                elif (i+j)%2==0:
                    current_pieces += "[#]"
                elif (i+j)%2!=0:
                    current_pieces += "[ ]"
            print(current_pieces)
        print(f"\n{self.current_side*'black' or 'white'}'s turn to play\n")

    def calculate_current_side_moves(self):
        for square in range(64):
            if self.board[square].piece_on_top and self.board[square].piece_on_top.col == self.current_side:
                self.board[square].piece_on_top.current_allowed_moves = []
                for move in self.board[square].piece_on_top.valid_moves(self):
                    if check_if_move_valid(move,square,self):
                        self.board[square].piece_on_top.current_allowed_moves.append(move)

    def index_to_chess_notation(self, index):
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]
        ranks = [1,2,3,4,5,6,7,8]
        if self.player_side == 0:
            return files[index % 8] + str(ranks[7-(index // 8)])
        elif self.player_side == 1:
            return files[7-(index % 8)] + str(ranks[index // 8])

    def move_piece(self,sq_one,sq_two, next_side=True):
        if next_side == "o-o" or next_side == "o-o-o":
            if self.current_side == 0:
                self.moves.append(next_side.replace("o", "O"))
            else:
                self.moves.append(next_side)
            self.next_move_dont_add = True
        else:
            self.current_side = not(self.current_side)
            if not(self.next_move_dont_add):
                original_pos = self.index_to_chess_notation(sq_one.position)
                middle_bit = " "
                if sq_two.piece_on_top:
                    middle_bit = " x "
                new_pos = self.index_to_chess_notation(sq_two.position)
                self.moves.append(original_pos + middle_bit + new_pos)
            else:
                self.next_move_dont_add = False
        sq_two.add_piece(sq_one.piece_on_top)
        sq_two.piece_on_top.moved = True
        sq_one.remove_piece()
        self.evaluate_position()

    def ai_move(self):
        squares_with_moves = []
        enemy_moves = get_all_moves_from_side(self.player_side, self)
        for square in get_all_moves_from_side(self.current_side, self, False, True):
            squares_with_moves.append(square)
        ran_sq = r.choice(squares_with_moves)
        chosen_squares = [ran_sq, ran_sq]
        chosen_moves = [False, False]
        for square in squares_with_moves:
            if square.position in enemy_moves:
                if not(chosen_moves[1]) or (square.piece_on_top.value>=chosen_squares[1].piece_on_top.value):
                    for move in square.piece_on_top.valid_moves(self):
                        if check_if_move_valid(move,square.position,self):
                            chosen_squares[1] = square
                            chosen_moves[1] = move
                            break
            for move in square.piece_on_top.valid_moves(self):
                if self.board[move].piece_on_top:
                    if not(chosen_moves[0]) or (self.board[move].piece_on_top.value>=self.board[chosen_moves[0]].piece_on_top.value):
                        if check_if_move_valid(move,square.position,self):
                            chosen_square = square
                            chosen_move = move
                            break

        to_highlight = False

        if not(chosen_moves[0]):
            chosen_moves[0] = r.choice(chosen_squares[0].piece_on_top.valid_moves(self))
        if chosen_moves[1]: #and (not(self.board[chosen_moves[0]].piece_on_top) or(chosen_squares[1].piece_on_top.value>self.board[chosen_moves[0]].piece_on_top.value)):
            self.current_highlighted = chosen_squares[1]
            perform_move(chosen_moves[1],self)
            to_highlight = chosen_moves[1]
        else:
            self.current_highlighted = chosen_squares[0]
            perform_move(chosen_moves[0], self)
            to_highlight = chosen_moves[0]

        if self.current_highlighted:
            self.current_highlighted.highlighted = False

        self.board[to_highlight].highlighted = True
        self.current_highlighted = self.board[to_highlight]
        self.display_board([],True)
        self.calculate_current_side_moves()

    def evaluate_position(self):
        evaluation = 0
        for square in self.board:
            if square.piece_on_top != None:
                if square.piece_on_top.col == 0:
                    evaluation += square.piece_on_top.value
                else:
                    evaluation -= square.piece_on_top.value
        self.eval = evaluation

    def set_up(self, side=0):
        self.player_side = side
        # opposing side
        self.board[0].add_piece(Rook(not(side)))
        self.board[1].add_piece(Knight(not(side)))
        self.board[2].add_piece(Bishop(not(side)))
        if side == 0:
            self.board[3].add_piece(Queen(not(side)))
            self.board[4].add_piece(King(not(side)))
        else:
            self.board[4].add_piece(Queen(not(side)))
            self.board[3].add_piece(King(not(side)))
        self.board[5].add_piece(Bishop(not(side)))
        self.board[6].add_piece(Knight(not(side)))
        self.board[7].add_piece(Rook(not(side)))
        self.board[8].add_piece(Pawn(not(side)))
        self.board[9].add_piece(Pawn(not(side)))
        self.board[10].add_piece(Pawn(not(side)))
        self.board[11].add_piece(Pawn(not(side)))
        self.board[12].add_piece(Pawn(not(side)))
        self.board[13].add_piece(Pawn(not(side)))
        self.board[14].add_piece(Pawn(not(side)))
        self.board[15].add_piece(Pawn(not(side)))

        # player side
        self.board[56].add_piece(Rook(side))
        self.board[57].add_piece(Knight(side))
        self.board[58].add_piece(Bishop(side))
        if side == 0:
            self.board[59].add_piece(Queen(side))
            self.board[60].add_piece(King(side))
        else:
            self.board[60].add_piece(Queen(side))
            self.board[59].add_piece(King(side))
        self.board[61].add_piece(Bishop(side))
        self.board[62].add_piece(Knight(side))
        self.board[63].add_piece(Rook(side))
        self.board[48].add_piece(Pawn(side))
        self.board[49].add_piece(Pawn(side))
        self.board[50].add_piece(Pawn(side))
        self.board[51].add_piece(Pawn(side))
        self.board[52].add_piece(Pawn(side))
        self.board[53].add_piece(Pawn(side))
        self.board[54].add_piece(Pawn(side))
        self.board[55].add_piece(Pawn(side))

        self.calculate_current_side_moves()

    def display_board(self, possible_moves=[], enemy_move=False):
        self.canv.clear()

        for square in range(64):
            if not(self.board[square].highlighted) or (self.board[square].highlighted and not(self.board[square].piece_on_top)):
                sq_col = ((square+(square//8))%2==0)*get_colour(4) or get_colour(5)
                self.canv.c.create_rectangle(square%8*(self.board_width/8), square//8*(self.board_width/8), square%8*(self.board_width/8)+self.board_width/8, square//8*(self.board_width/8)+self.board_width/8, fill=sq_col, outline="")
            elif not(enemy_move):
                self.canv.c.create_rectangle(square%8*(self.board_width/8), square//8*(self.board_width/8), square%8*(self.board_width/8)+self.board_width/8, square//8*(self.board_width/8)+self.board_width/8, fill=get_colour(6), outline=get_colour(0))
            else:
                self.canv.c.create_rectangle(square % 8 * (self.board_width / 8), square // 8 * (self.board_width / 8),
                                             square % 8 * (self.board_width / 8) + self.board_width / 8,
                                             square // 8 * (self.board_width / 8) + self.board_width / 8,
                                             fill=get_colour(1), outline=get_colour(0))

        for index in range(64):
            square = self.board[index]
            x = index%8*(self.board_width/8)+(self.board_width/16)
            y = index//8*(self.board_width/8)+(self.board_width/16)
            self.board[index].highlighted = False
            if square.piece_on_top:
                piece = Image.open(f"pieces/{self.piece_set}/"+square.piece_on_top.get_piece_image())
                piece = piece.resize((self.board_width//11,self.board_width//11), Image.ANTIALIAS)
                piece = ImageTk.PhotoImage(piece)
                self.canv.images.append([x,y,piece])
        self.canv.display()

        if len(possible_moves)>0 and self.current_highlighted.piece_on_top.col == self.current_side and self.current_highlighted.piece_on_top.col == self.player_side:
            for move in possible_moves:
                if not(self.board[move].piece_on_top):
                    self.canv.c.create_rectangle((self.board_width/10)/2+move%8*(self.board_width/8), (self.board_width/10)/2+move//8*(self.board_width/8), move%8*(self.board_width/8)+self.board_width/8-self.board_width/20, move//8*(self.board_width/8)+self.board_width/8-self.board_width/20, fill=get_colour(7), outline="")
                else:
                    self.canv.c.create_rectangle(move%8*(self.board_width/8), move//8*(self.board_width/8), move%8*(self.board_width/8)+self.board_width/8, move//8*(self.board_width/8)+self.board_width/8, fill="", outline=get_colour(8))
                self.current_valid_moves.append(move)
        elif self.current_side != self.player_side and self.current_side<2:
            self.ai_move()


if __name__ == "__main__":
    my_board = Board()
    my_board.set_up(0)
    my_board.move_piece(my_board.board[8],my_board.board[16])
    my_board.console_log_board()