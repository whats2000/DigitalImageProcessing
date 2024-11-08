import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR, SECONDARY_THEME
from utils import open_image, remove_compare_image, save_image

if TYPE_CHECKING:
    from app import ImageProcessorApp


def create_hw3_panel(app: 'ImageProcessorApp', container: tk.Frame):
    """
    Placeholder for HW3 panel for future operations.
    """
    panel = tk.Frame(container, bg=MAIN_THEME)
    return panel
