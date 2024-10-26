import tkinter as tk

from app import ImageProcessorApp
from config import MAIN_THEME

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.configure(background=MAIN_THEME)
    root.mainloop()
