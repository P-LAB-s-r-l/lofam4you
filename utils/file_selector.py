import tkinter as tk
from tkinter import filedialog
from constants import SELECTED_PATH_FILE

def select_file():
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.focus_force()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

if __name__ == "__main__":
    selected_file = select_file()
    with open(SELECTED_PATH_FILE, "w") as f:
        f.write(selected_file)
