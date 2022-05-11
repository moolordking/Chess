
class Piece(object):
    def __init__(self, piece_type, col):
        self.piece_type = piece_type
        self.col = col
        self.position = [0,0]
    def set_position(self,pos):
        self.position = [pos[0], pos[1]]
    def show_moves(self):
        return None

if __name__ == "__main__":
    my_piece = Piece("king", 0)
    print((my_piece.col*"black "or"white ") + my_piece.piece_type)
