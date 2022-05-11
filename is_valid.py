
 #=============================================================================#
 #
 #                            ~~Validation module~~
 #                       Module written by Malachi Bance
 #                                                                  [09/05/22]
 # Known bugs: none
 #=============================================================================#

def v_length(data, len_to_check, len_option=1):
    # validates length with three options, defaulting to equal to
    # option 1 validates if data equal to length
    if   len_option == 1 : return len(data) == len_to_check
    # option 2 validates if data larger or equal to length
    elif len_option == 2 : return len(data) >= len_to_check
    # option 3 validates if data less than length
    elif len_option == 3 : return len(data) <  len_to_check

def v_range(data, lo, hi):
    # validates range, between min and max
    return (data >= lo) and (data < hi)

if __name__ == "__main__":
    print(v_length("hello", 5, 1))  # if "hello" has length of 5
    print(v_length("hello", 6, 1))  # if "hello" has length of 6
    print(v_length("hello", 5, 3))  # if "hello" has length of less than 5
    print()
    print(v_range(5, 1, 4))  # if 5 is within range 1-4
    print(v_range(5, 1, 5))  # if 5 is within range 1-5
    print(v_range(5, 5, 6))  # if 5 is within range 5-6
