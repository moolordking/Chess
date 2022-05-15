
from is_valid import *

class Piece(object):
    def __init__(self, piece_type, col):
        self.piece_type = piece_type
        self.col = col
        self.position = 0
        self.value = 0
        self.moved = False
        self.possible_valid_move_indices = []
    def set_position(self,pos):
        self.position = pos
    def show_moves(self):
        return None
    def get_piece_image(self):
        return (self.col*"b_" or "w_") + self.piece_type.lower() + ".png"
    def valid_moves(self,chess_board):
        return self.possible_valid_move_indices
    def check_empty_space(self, position, num, leftordown, chess_board, expected=0, diagonal=False):
        if diagonal:
            if num<0:
                return position+num>0 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col) and ((position+num)//8 != (position)//8) and (position+num)//8 == ((position//8)-(diagonal))
            else:
                return position+num<64 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col) and ((position+num)//8 != (position)//8) and (position+num)//8 == ((position//8)+(diagonal))
        elif leftordown:
            if num<0:
                return ((position+num)//8 == (position)//8)+expected and position+num>0 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col)
            else:
                return ((position+num)//8 == (position)//8)+expected and position+num<64 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col)
        else:
            if num<0:
                return ((position+num)%8 == (position)%8)+expected and position+num>0 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col)
            else:
                return ((position+num)%8 == (position)%8)+expected and position+num<64 and (not(chess_board.board[position+num].piece_on_top) or chess_board.board[position+num].piece_on_top.col != self.col)

class Rook(Piece):
    def __init__(self, col):
        super().__init__("rook",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 5
        self.possible_valid_move_indices = []

    def valid_moves(self,chess_board):
        self.possible_valid_move_indices = []

        for y in range(1,8):
            if self.check_empty_space(self.position, y*8, False, chess_board):
                self.possible_valid_move_indices.append(self.position+(y*8))
            if v_range(self.position+(y*8),0,64) and chess_board.board[self.position+(y*8)].piece_on_top:
                break
        for y in range(-1,-8,-1):
            if self.check_empty_space(self.position, y*8, False, chess_board):
                self.possible_valid_move_indices.append(self.position+(y*8))
            if v_range(self.position+(y*8),0,64) and chess_board.board[self.position+(y*8)].piece_on_top:
                break
        for x in range(1,8):
            if self.check_empty_space(self.position, x, True, chess_board):
                self.possible_valid_move_indices.append(self.position+x)
            if v_range(self.position+x,0,64) and chess_board.board[self.position+x].piece_on_top:
                break
        for x in range(-1,-8,-1):
            if self.check_empty_space(self.position, x, True, chess_board):
                self.possible_valid_move_indices.append(self.position+x)
            if v_range(self.position+x,0,64) and chess_board.board[self.position+x].piece_on_top:
                break

        return self.possible_valid_move_indices

class Knight(Piece):
    def __init__(self, col):
        super().__init__("knight",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 3
        self.possible_valid_move_indices = []

class Bishop(Piece):
    def __init__(self, col):
        super().__init__("bishop",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 3
        self.possible_valid_move_indices = []

    def valid_moves(self,chess_board):
        self.possible_valid_move_indices = []

        for i in range (1,8):
            if self.check_empty_space(self.position, (i*8)+i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(i*8)+i)
            else:
                break
            if v_range(self.position+(i*8)+i,0,64) and chess_board.board[self.position+(i*8)+i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (i*8)-i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(i*8)-i)
            else:
                break
            if v_range(self.position+(i*8)-i,0,64) and chess_board.board[self.position+(i*8)-i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (-i*8)+i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(-i*8)+i)
            else:
                break
            if v_range(self.position+(-i*8)+i,0,64) and chess_board.board[self.position+(-i*8)+i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (-i*8)-i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(-i*8)-i)
            else:
                break
            if v_range(self.position+(-i*8)-i,0,64) and chess_board.board[self.position+(-i*8)-i].piece_on_top:
                break

        return self.possible_valid_move_indices

class Queen(Piece):
    def __init__(self, col):
        super().__init__("queen",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 9
        self.possible_valid_move_indices = []

    def valid_moves(self,chess_board):
        self.possible_valid_move_indices = []

        for y in range(1,8):
            if self.check_empty_space(self.position, y*8, False, chess_board):
                self.possible_valid_move_indices.append(self.position+(y*8))
            if v_range(self.position+(y*8),0,64) and chess_board.board[self.position+(y*8)].piece_on_top:
                break
        for y in range(-1,-8,-1):
            if self.check_empty_space(self.position, y*8, False, chess_board):
                self.possible_valid_move_indices.append(self.position+(y*8))
            if v_range(self.position+(y*8),0,64) and chess_board.board[self.position+(y*8)].piece_on_top:
                break
        for x in range(1,8):
            if self.check_empty_space(self.position, x, True, chess_board):
                self.possible_valid_move_indices.append(self.position+x)
            if v_range(self.position+x,0,64) and chess_board.board[self.position+x].piece_on_top:
                break
        for x in range(-1,-8,-1):
            if self.check_empty_space(self.position, x, True, chess_board):
                self.possible_valid_move_indices.append(self.position+x)
            if v_range(self.position+x,0,64) and chess_board.board[self.position+x].piece_on_top:
                break
        # diagonals
        for i in range (1,8):
            if self.check_empty_space(self.position, (i*8)+i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(i*8)+i)
            else:
                break
            if v_range(self.position+(i*8)+i,0,64) and chess_board.board[self.position+(i*8)+i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (i*8)-i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(i*8)-i)
            else:
                break
            if v_range(self.position+(i*8)-i,0,64) and chess_board.board[self.position+(i*8)-i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (-i*8)+i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(-i*8)+i)
            else:
                break
            if v_range(self.position+(-i*8)+i,0,64) and chess_board.board[self.position+(-i*8)+i].piece_on_top:
                break
        for i in range (1,8):
            if self.check_empty_space(self.position, (-i*8)-i, False, chess_board, 1, i):
                self.possible_valid_move_indices.append(self.position+(-i*8)-i)
            else:
                break
            if v_range(self.position+(-i*8)-i,0,64) and chess_board.board[self.position+(-i*8)-i].piece_on_top:
                break

        return self.possible_valid_move_indices


class King(Piece):
    def __init__(self, col):
        super().__init__("king",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 900
        self.possible_valid_move_indices = []

    def valid_moves(self,chess_board):
        self.possible_valid_move_indices = []

        if self.check_empty_space(self.position, -1, True, chess_board):
            self.possible_valid_move_indices.append(self.position-1)
        if self.check_empty_space(self.position, +1, True, chess_board):
            self.possible_valid_move_indices.append(self.position+1)
        if self.check_empty_space(self.position, +8, False, chess_board):
            self.possible_valid_move_indices.append(self.position+8)
        if self.check_empty_space(self.position, -8, False, chess_board):
            self.possible_valid_move_indices.append(self.position-8)
        if self.check_empty_space(self.position, -9, False, chess_board, 1, 1):
            self.possible_valid_move_indices.append(self.position-9)
        if self.check_empty_space(self.position, -7, False, chess_board, 1, 1):
            self.possible_valid_move_indices.append(self.position-7)
        if self.check_empty_space(self.position, +9, False, chess_board, 1, 1):
            self.possible_valid_move_indices.append(self.position+9)
        if self.check_empty_space(self.position, +7, False, chess_board, 1, 1):
            self.possible_valid_move_indices.append(self.position+7)
            
        return self.possible_valid_move_indices

class Pawn(Piece):
    def __init__(self, col):
        super().__init__("pawn",col)
        self.col = col
        if self.col == 0:
            self.piece_type = self.piece_type.upper()
        self.value = 1
        self.possible_valid_move_indices = []

    def valid_moves(self,chess_board):
        self.possible_valid_move_indices = []
        nop = 1
        if self.col == 1 and chess_board.player_side == 0:
            nop = -1
        if self.col == 1 and chess_board.player_side == 1:
            nop = 1
        if self.col == 0 and chess_board.player_side == 1:
            nop = -1
        if not(chess_board.board[self.position-(8*nop)].piece_on_top):
            self.possible_valid_move_indices.append(self.position-(8*nop))
            if not(chess_board.board[self.position-(16*nop)].piece_on_top) and not(self.moved):
                self.possible_valid_move_indices.append(self.position-(16*nop))
        if chess_board.board[self.position-(9*nop)].piece_on_top and chess_board.board[self.position-(9*nop)].piece_on_top.col != self.col:
            self.possible_valid_move_indices.append(self.position-(9*nop))
        if chess_board.board[self.position-(7*nop)].piece_on_top and chess_board.board[self.position-(7*nop)].piece_on_top.col != self.col:
            self.possible_valid_move_indices.append(self.position-(7*nop))

        return self.possible_valid_move_indices

if __name__ == "__main__":
    my_piece = Piece("king", 0)
    my_other_piece = King(0)
    print((my_piece.col*"black "or"white ") + my_piece.piece_type)
    print(my_other_piece.piece_type)
