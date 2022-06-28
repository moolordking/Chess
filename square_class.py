
from piece_classes import *

class Square(object):
    def __init__(self,position,col):
        self.position = position
        self.col = col
        self.piece_on_top = None
        self.highlighted = False
    def add_piece(self, piece):
        self.piece_on_top = piece
        self.piece_on_top.position = self.position
    def remove_piece(self):
        self.piece_on_top = None

if __name__ == "__main__":
    my_piece = Piece("king", 0)
    my_square = Square(0, 0)
    my_square.piece_on_top = my_piece
    print(my_square.piece_on_top.piece_type)

