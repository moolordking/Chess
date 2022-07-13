
# handle settings
import file_handling as fh

def get_settings(num=0):
    loc = "settings.txt"
    settings = []
    settings = fh.read_line_from_file(loc, num + 5).split(";")[0].replace(" ", "")[1:-1]
    return settings

def set_settings(num=0, data=""):
    loc = "settings.txt"
    settings = []
    settings = fh.write_to_line(loc, num + 5, "["+data+"] ;" + fh.read_line_from_file(loc, num + 5).split(";")[1])

set_settings(1, "embers")