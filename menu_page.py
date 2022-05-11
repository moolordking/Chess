
from tkinter import *
# module for colours and graphics - including fonts
from colours_and_graphics import *

def create_gui():
    #create window
    root = Tk()
    root.title("Menu")
    root.geometry("640x400+600+200")
    root.configure(background=get_colour(0))
    # display header
    header_message = Label(root, text="Chess")
    header_message.config(font=(get_font(), 40), fg=get_colour(1), bg=get_colour(0))
    header_message.grid(row=0, column=0, columnspan=2, sticky="W", padx=240, pady=30)


    root.mainloop()

if __name__ == "__main__":
    create_gui()