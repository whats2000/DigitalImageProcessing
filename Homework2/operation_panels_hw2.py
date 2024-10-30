import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR

if TYPE_CHECKING:
    from app import ImageProcessorApp

def create_hw2_panel(app: 'ImageProcessorApp', container: tk.Frame):
    """
    Placeholder for HW2 panel for future operations.
    """
    panel = tk.Frame(container, bg=MAIN_THEME)
    return panel