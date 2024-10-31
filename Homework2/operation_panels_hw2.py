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
    _setup_bar_test_buttons_frame(app, panel)
    _setup_lenna_buttons_frame(app, panel)
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

"""
2. The white bars in the test pattern shown below (BarTest.tif) are 7 pixels wide and 210
pixels high. The separation between bars is 17 pixels. Please apply the following filters
to this image and show the results:
(a) A 7x7 arithmetic mean filter?
(b) A 3x3 arithmetic mean filter?
(c) A 7x7 median filter?
(d) A 3x3 median filter?
"""
def _setup_bar_test_buttons_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for applying filters to the test pattern
    """
    # Create labels for the mask buttons
    mask_text = tk.Label(
        parent_frame,
        text="Filters for test pattern",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    mask_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)
    app.arithmetic_mean_7x7_button = tk.Button(
        button_frame,
        text="7x7 Arithmetic Mean",
        command=lambda : app.operations.apply_averaging_mask(7)
    )
    app.arithmetic_mean_3x3_button = tk.Button(
        button_frame,
        text="3x3 Arithmetic Mean",
        command=lambda : app.operations.apply_averaging_mask(3)
    )
    button_frame_2 = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame_2.pack(anchor="w", pady=5)
    app.median_7x7_button = tk.Button(
        button_frame_2,
        text="7x7 Median",
        command=lambda : app.operations.apply_median_mask(7)
    )
    app.median_3x3_button = tk.Button(
        button_frame_2,
        text="3x3 Median",
        command=lambda : app.operations.apply_median_mask(3)
    )
    app.arithmetic_mean_7x7_button.pack(side=tk.LEFT)
    app.arithmetic_mean_3x3_button.pack(side=tk.LEFT, padx=10)
    app.median_7x7_button.pack(side=tk.LEFT)
    app.median_3x3_button.pack(side=tk.LEFT, padx=10)

"""
3. “Lenna” is a famous example of digital image processing. In order to have a further
understanding of it, please do the following steps:
(a) Obtain the 2D-FFT of the image “Lenna.tif”, and display the spectrum image of log|F(u, v)|.
(b) Magnitude and Phase images: Do 2D-FFT to obtain the magnitude and phase of the image. 
    Display its “magnitude-only image” and “phase-only image” by applying inverse 2D FFT.
"""
def _setup_lenna_buttons_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for applying filters to the test pattern
    """
    # Create labels for the mask buttons
    mask_text = tk.Label(
        parent_frame,
        text="Filters for Lenna",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    mask_text.pack(anchor="w", pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.pack(anchor="w", pady=5)
    app.fft_button = tk.Button(
        button_frame,
        text="2D-FFT",
        command=app.operations.apply_fft
    )
    app.fft_magnitude_only_button = tk.Button(
        button_frame,
        text="Magnitude Only",
        command=app.operations.apply_inverse_fft_magnitude_only
    )
    button_frame_2 = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame_2.pack(anchor="w", pady=5)
    app.fft_phase_only_button = tk.Button(
        button_frame_2,
        text="Phase Only",
        command=app.operations.apply_inverse_fft_phase_only
    )
    app.fft_button.pack(side=tk.LEFT)
    app.fft_magnitude_only_button.pack(side=tk.LEFT, padx=10)
    app.fft_phase_only_button.pack(side=tk.LEFT)