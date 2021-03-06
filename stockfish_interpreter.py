from stockfish import Stockfish

stockfishy = Stockfish(path="stockfish_15_win_x64_avx2/stockfish_15_x64_avx2",
                       parameters={"Skill Level": -5})
stockfishy.update_engine_parameters({
    "Hash": 256,
    "UCI_LimitStrength": "true"
})

def sf_move_piece(move=1):
    global stockfishy
    if move == 1:
        return

    stockfishy.make_moves_from_current_position([move])
    # print("**"+stockfishy.get_best_move()+"**")

def sf_best_move():
    global stockfishy
    return stockfishy.get_best_move()

def sf_skill_level(level):
    stockfishy.update_engine_parameters({"Skill Level": level})

if __name__ == "__main__":
    stockfishy.update_engine_parameters({"Hash": 256})
    sf_move_piece()

    print(stockfishy.get_best_move())
    print(stockfishy.is_move_correct('a1a3'))