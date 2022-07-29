
# handle settings
import wx
import file_handling as fh
from tkinter import *
from tkinter import font
from colours_and_graphics import *

def get_settings(num=0):
    loc = "settings.txt"
    settings = []
    settings = fh.read_line_from_file(loc, num + 5).split(";")[0].replace(" ", "")[1:-1]
    return settings

def set_settings(num=0, data=""):
    loc = "settings.txt"
    settings = []
    settings = fh.write_to_line(loc, num + 5, "["+data+"] ;" + fh.read_line_from_file(loc, num + 5).split(";")[1])

def settings_gui(root_to_destroy=None):
    if root_to_destroy:
        root_to_destroy.destroy()
    root = Tk()
    app = wx.App(False)
    root.title("Settings")
    dimensions = [400,500]
    root.geometry(f"{dimensions[0]}x{dimensions[1]}+{(wx.GetDisplaySize()[0]//2)-int(dimensions[0]/2)}+{(wx.GetDisplaySize()[1]//2)-int(dimensions[1]/2)}")
    root.configure(background=get_colour(0))
    root.iconbitmap('favicon.ico')
    root.resizable(False, False)

    header_message = Label(root, text="Settings")
    header_message.config(font=(get_font(), 20), fg=get_colour(1), bg=get_colour(0), width=25)
    header_message.grid(row=0, column=0, columnspan=2, sticky="W")

    setting_1_text = Label(root, text="AI difficulty")
    setting_1_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(5))
    setting_1_text.grid(row=1, column=0, sticky="W")

    setting_1_entry = Entry(root, width=10)
    setting_1_entry.insert(END, sh.get_settings(0))
    setting_1_entry.config(font=(get_font(), 15))
    setting_1_entry.grid(row=1, column=1)

    setting_2_text = Label(root, text="Theme")
    setting_2_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(2))
    setting_2_text.grid(row=2, column=0, sticky="W")

    setting_2_entry = Entry(root, width=10)
    setting_2_entry.insert(END, sh.get_settings(1))
    setting_2_entry.config(font=(get_font(), 15))
    setting_2_entry.grid(row=2, column=1)

    setting_3_text = Label(root, text="Piece set")
    setting_3_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(5))
    setting_3_text.grid(row=3, column=0, sticky="W")

    setting_3_entry = Entry(root, width=10)
    setting_3_entry.insert(END, sh.get_settings(2))
    setting_3_entry.config(font=(get_font(), 15))
    setting_3_entry.grid(row=3, column=1)

    setting_4_text = Label(root, text="starting colour")
    setting_4_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(2))
    setting_4_text.grid(row=4, column=0, sticky="W")

    setting_4_entry = Entry(root, width=10)
    setting_4_entry.insert(END, sh.get_settings(3))
    setting_4_entry.config(font=(get_font(), 15))
    setting_4_entry.grid(row=4, column=1)

    setting_5_text = Label(root, text="Clock")
    setting_5_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(5))
    setting_5_text.grid(row=5, column=0, sticky="W")

    setting_5_entry = Entry(root, width=10)
    setting_5_entry.insert(END, sh.get_settings(4))
    setting_5_entry.config(font=(get_font(), 15))
    setting_5_entry.grid(row=5, column=1)

    setting_6_text = Label(root, text="Alternate stockfish")
    setting_6_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(2))
    setting_6_text.grid(row=6, column=0, sticky="W")

    setting_6_entry = Entry(root, width=10)
    setting_6_entry.insert(END, sh.get_settings(5))
    setting_6_entry.config(font=(get_font(), 15))
    setting_6_entry.grid(row=6, column=1)

    setting_7_text = Label(root, text="Board width")
    setting_7_text.config(font=(get_font(), 15), fg=get_colour(1), bg=get_colour(5))
    setting_7_text.grid(row=7, column=0, sticky="W")

    setting_7_entry = Entry(root, width=10)
    setting_7_entry.insert(END, sh.get_settings(6))
    setting_7_entry.config(font=(get_font(), 15))
    setting_7_entry.grid(row=7, column=1)

    button_font = font.Font(family=get_font(), size=10, weight="bold")

    setting_vals = [setting_1_entry, setting_2_entry, setting_3_entry, setting_4_entry, setting_5_entry, setting_6_entry, setting_7_entry]

    apply_button = Button(root, text="Apply Settings", width=20, height=2, command=lambda: apply_settings(root, setting_vals))
    apply_button.config(fg=get_colour(4), bg=get_colour(1), borderwidth=0)
    apply_button['font'] = button_font
    apply_button.grid(row=8, column=0, columnspan=2, pady=200)

    root.mainloop()

def apply_settings(root, vals):
    for i,val in enumerate(vals):
        set_settings(i, val.get())
    root.destroy()

if __name__ == "__main__":
    set_settings(4, "False")
    settings_gui()

