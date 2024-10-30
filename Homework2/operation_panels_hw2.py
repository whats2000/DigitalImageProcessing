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
    _setup_mask_buttons_frame(app, panel)
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

"""
(a) Download the images ‘pirate_a.raw’ and ‘pirate_b.raw’ as shown above (512x512, 256
grayscale). Apply a 3x3 averaging mask to both of the images and make a comparison
according to your result.
(b) Repeat (a), but apply a 3x3 median filter rather than the averaging mask to both of the
images. Again, compare these two resultant images and give your explanation.
(c) Choose the best-improved image you can obtain from (a) and (b), and apply the
Laplacian mask to this image. Display the filtered result and compare it with the
original image.
"""
def  _setup_mask_buttons_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for applying masks to images
    """
    # Create labels for the mask buttons
    mask_text = tk.Label(
        parent_frame,
        text="Masks for denoising",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    mask_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)
    app.averaging_mask_button = tk.Button(
        button_frame,
        text="Averaging Mask",
        command=app.operations.apply_averaging_mask
    )
    app.median_mask_button = tk.Button(
        button_frame,
        text="Median Mask",
        command=app.operations.apply_median_mask
    )
    button_frame_2 = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame_2.pack(anchor="w", pady=5)
    app.laplacian_mask_button = tk.Button(
        button_frame_2,
        text="Apply Laplacian",
        command=app.operations.apply_laplacian_mask
    )
    app.averaging_mask_button.pack(side=tk.LEFT)
    app.median_mask_button.pack(side=tk.LEFT, padx=10)
    app.laplacian_mask_button.pack(side=tk.LEFT)
    return button_frame