import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR

if TYPE_CHECKING:
    from app import ImageProcessorApp


def create_hw3_panel(app: 'ImageProcessorApp', container: tk.Frame):
    """
    Placeholder for HW3 panel for future operations.
    """
    panel = tk.Frame(container, bg=MAIN_THEME)
    _setup_rgb_buttons_frame(app, panel)
    _setup_hsi_buttons_frame(app, panel)
    return panel


"""
Obtain its “Red component image”, “Green component
image”, and “Blue component image” and display them as
24-bit color images respectively.
"""


def _setup_rgb_buttons_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for RGB operations
    """
    # Create labels for the rgb operations
    rgb_operation_text = tk.Label(
        parent_frame,
        text="RGB Operations",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    rgb_operation_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)

    # Buttons for RGB operations
    app.red_button = tk.Button(
        button_frame,
        text="Red",
        command=lambda: app.operations.rgb_image('red')
    )
    app.green_button = tk.Button(
        button_frame,
        text="Green",
        command=lambda: app.operations.rgb_image('green')
    )
    app.blue_button = tk.Button(
        button_frame,
        text="Blue",
        command=lambda: app.operations.rgb_image('blue')
    )
    app.red_button.pack(side=tk.LEFT)
    app.green_button.pack(side=tk.LEFT, padx=10)
    app.blue_button.pack(side=tk.LEFT)


"""
According to the definition of RGB model and HSI model, try
to convert RGB to HSI model, and display its Hue,
Saturation, and Intensity components as gray-level images
respectively.
"""

def _setup_hsi_buttons_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for HSI operations
    """
    # Create labels for the hsi operations
    hsi_operation_text = tk.Label(
        parent_frame,
        text="HSI Operations",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    hsi_operation_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)

    # Buttons for HSI operations
    app.hue_button = tk.Button(
        button_frame,
        text="Hue",
        command=lambda: app.operations.hsi_image('hue')
    )
    app.saturation_button = tk.Button(
        button_frame,
        text="Saturation",
        command=lambda: app.operations.hsi_image('saturation')
    )
    app.intensity_button = tk.Button(
        button_frame,
        text="Intensity",
        command=lambda: app.operations.hsi_image('intensity')
    )
    app.hue_button.pack(side=tk.LEFT)
    app.saturation_button.pack(side=tk.LEFT, padx=10)
    app.intensity_button.pack(side=tk.LEFT)