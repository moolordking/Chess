import os

def create_file(file_path="text.txt"):
    if not(os.path.isfile(file_path)):
        with open(file_path, "w") as fp:
            fp.write("")

def delete_file(file_path="text.txt"):
    if os.path.isfile(file_path):
        os.remove(file_path)

def read_line_from_file(file_path="text.txt", line=0):
    if os.path.isfile(file_path):
        with open(file_path, "r") as fp:
            return fp.readlines()[line]

def read_file(file_path="text.txt"):
    if os.path.isfile(file_path):
        with open(file_path, "w") as fp:
            return fp.read()

