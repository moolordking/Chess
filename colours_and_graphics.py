import file_handling as fh

def get_colour(num=0, scheme="frosty"):
    loc = "themes/"+scheme+".txt"
    cols = []
    col = fh.read_line_from_file(loc, num + 5).split(";")[0][1:-2]
    return col
    # if num == 0 : return "#0B0C10" # background
    # if num == 1 : return "#FFFFFF" # text
    # if num == 2 : return "#1F2833" # background alternative
    # if num == 3: return "#5beeff"  # button and standout colour
    #
    # if num == 4: return "#1F2833" # chess board light colour
    # if num == 5: return "#131921" # chess board dark  colour
    # if num == 6: return "#99eeff" # selected colour
    # if num == 7: return "#8899ff" # possible move colour
    # if num == 8: return "#DD9988" # capture move colour

def get_font():
    return "Courier New"

if __name__ == "__main__":
    cols = []
    for no in range(9):
        line = fh.read_line_from_file("themes/frosty.txt",no+5).split(";")[0][1:-2]
        cols.append(line)
    print(cols)