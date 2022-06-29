
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
            if chess_board.check_if_move_valid(index - 1, index - 2, chess_board):
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
            if chess_board.check_if_move_valid(index + 1, index + 2, chess_board):
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