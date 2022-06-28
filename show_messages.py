
#from tkinter import *
from tkinter import messagebox

# =============================================================================#
#
#                            ~~Show Message module~~
#                       Module written by Malachi Bance
#                                                                  [16/05/22]
# Known bugs: none
# =============================================================================#

def s_message(message, message_title="", which_one=0, message_type=0):
    try:
        # options for button
        if message_type == 0:
            message_type = "ok"
        elif message_type == 1:
            message_type = "okcancel"
        elif message_type == 2:
            message_type = "yesno"
        # displaying message
        if which_one == 0:
            messagebox.showerror(title=message_title, message=message, type=message_type)
        elif which_one == 1:
            messagebox.showwarning(title=message_title, message=message, type=message_type)
        elif which_one == 2:
            messagebox.showinfo(title=message_title, message=message, type=message_type)
    except:
        print(f"error showing '{message}'")


if __name__ == "__main__":
    s_message("this is an error message", "error", 0)
