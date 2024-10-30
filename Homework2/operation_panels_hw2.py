import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR, SECONDARY_THEME
from utils import open_image, remove_compare_image, save_image

if TYPE_CHECKING:
    from app import ImageProcessorApp

def create_hw2_panel(app: 'ImageProcessorApp', container: tk.Frame):
    """
    Placeholder for HW2 panel for future operations.
    """
    panel = tk.Frame(container, bg=MAIN_THEME)
    _setup_load_save_compare_buttons(app, panel)
    return panel

def _setup_load_save_compare_buttons(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for loading and saving the compare image
    """
    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)

    # Buttons for loading and saving the compare image
    app.load_compare_button = tk.Button(
        button_frame,
        fg=MAIN_FONT_COLOR,
        bg=SECONDARY_THEME,
        text="Open 2nd Image",
        command=lambda: open_image(app, is_compare_image=True)
    )
    app.remove_compare_button = tk.Button(
        button_frame,
        fg=MAIN_FONT_COLOR,
        bg=SECONDARY_THEME,
        text="Remove 2nd Image",
        command=lambda: remove_compare_image(app)
    )
    app.load_compare_button.pack(side=tk.LEFT)
    app.remove_compare_button.pack(side=tk.LEFT, padx=10)

    second_button_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    second_button_frame.pack(anchor="w", pady=5)
    app.download_compare_button = tk.Button(
        second_button_frame,
        fg=MAIN_FONT_COLOR,
        bg=SECONDARY_THEME,
        text="Save 2nd Image",
        command=lambda: save_image(app, is_compare_image=True)
    )
    app.download_compare_button.pack(side=tk.LEFT)