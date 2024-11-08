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
    _setup_complement_histogram_equalization_frame(app, panel)
    _setup_smoothing_sharpening_frame(app, panel)
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


"""
Do color complements to enhance the detail in the image by
using RGB model.
"""
"""
Do histogram equalization for all RGB components and
display the original and processed images for comparison
"""

def _setup_complement_histogram_equalization_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for complement operations and histogram equalization
    """
    # Create labels for the complement operations
    complement_operation_text = tk.Label(
        parent_frame,
        text="Complement and Histogram Equalization",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    complement_operation_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)

    # Buttons for complement operations
    app.complement_button = tk.Button(
        button_frame,
        text="Complement",
        command=lambda: app.operations.complement_image()
    )
    app.histogram_button = tk.Button(
        button_frame,
        text="Histogram Equalization",
        command=lambda: app.operations.rgb_histogram_equalization()
    )
    app.complement_button.pack(side=tk.LEFT)
    app.histogram_button.pack(side=tk.LEFT, padx=10)


"""
Please do image smoothing with a 5x5 average kernel and
sharping with the Laplacian to this “Lenna” image by using
RGB and HSI models respectively. Display the results and
also show the difference from the original one. Please also
show the difference between results obtained by using RGB
and HSI models.
"""


def _setup_smoothing_sharpening_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for smoothing and sharpening operations
    """
    # Create labels for the smoothing and sharpening operations
    smoothing_sharpening_text = tk.Label(
        parent_frame,
        text="Smoothing and Sharpening",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    smoothing_sharpening_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)

    # Buttons for smoothing and sharpening operations
    app.rgb_image_smoothing_button = tk.Button(
        button_frame,
        text="5x5 Average",
        command=lambda: app.operations.apply_averaging_mask(5)
    )
    app.rgb_image_sharpening_button_rgb_model = tk.Button(
        button_frame,
        text="Sharpening RGB",
        command=lambda: app.operations.apply_sharpening_mask('rgb')
    )
    app.rgb_image_smoothing_button.pack(side=tk.LEFT)
    app.rgb_image_sharpening_button_rgb_model.pack(side=tk.LEFT, padx=10)

    # Create a frame to hold the buttons
    button_frame_2 = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame_2.pack(anchor="w", pady=5)

    app.rgb_image_sharpening_button_hsi_model = tk.Button(
        button_frame_2,
        text="Sharpening HSI",
        command=lambda: app.operations.apply_sharpening_mask('hsi')
    )
    app.rgb_image_sharpening_button_hsi_model.pack(side=tk.LEFT)


"""
Find some proper masks of saturation and hue component
images to this “Lenna” image so that the blue feathers of
the hat can be segmented by simple logical or arithmetic
operations of these 2 images. Demonstration of images
from each step as well as the final result is required.
"""