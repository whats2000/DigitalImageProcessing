import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR

if TYPE_CHECKING:
    from app import ImageProcessorApp

def create_hw1_panel(app: 'ImageProcessorApp', container: tk.Frame) -> tk.Frame:
    """
    The homework 1 panel with all the operations.
    """
    panel = tk.Frame(container, bg=MAIN_THEME)
    _setup_contrast_brightness_frame(app, panel)
    _setup_resize_rotate_frame(app, panel)
    _setup_gray_level_slicing_frame(app, panel)
    _setup_histogram_equalization_frame(app, panel)
    _setup_bit_plane_frame(app, panel)
    _setup_smoothing_sharpening_frame(app, panel)
    return panel

def _setup_contrast_brightness_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for adjusting alpha and beta values for brightness/contrast.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Adjust brightness and contrast",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Menu for selecting the brightness algorithm
    menu_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    menu_frame.pack(anchor="w", pady=5)
    app.brightness_menu = tk.OptionMenu(
        menu_frame,
        app.brightness_algorithm,
        "Linear",
        "Exponential",
        "Logarithmic",
    )
    app.brightness_apply_button = tk.Button(
        menu_frame,
        text="Apply",
        width=10,
        command=app.operations.apply_brightness_algorithm,
    )
    app.brightness_menu.pack(side=tk.LEFT, padx=5)
    app.brightness_apply_button.pack(side=tk.LEFT, padx=5)

    # Alpha frame for adjusting
    alpha_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    alpha_frame.pack(anchor="w", pady=5)
    alpha_label = tk.Label(alpha_frame, text="a value", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.alpha_input = tk.Entry(
        alpha_frame,
        textvariable=app.brightness_alpha,
        width=10,
    )
    alpha_label.pack(side=tk.LEFT, padx=5)
    app.alpha_input.pack(side=tk.LEFT, padx=5)

    # Beta frame for adjusting
    beta_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    beta_frame.pack(anchor="w", pady=5)
    beta_label = tk.Label(beta_frame, text="b value", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.beta_input = tk.Entry(
        beta_frame,
        textvariable=app.brightness_beta,
        width=10,
    )
    beta_label.pack(side=tk.LEFT, padx=5)
    app.beta_input.pack(side=tk.LEFT, padx=5)

def _setup_resize_rotate_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for resizing and rotating images.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Resize and Rotate",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Resize scale input box and button
    resize_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    resize_frame.pack(anchor="w", pady=5)
    app.resize_input = tk.Entry(
        resize_frame,
        textvariable=app.resize_scale,
        width=10,
    )
    app.resize_input.pack(side=tk.LEFT, padx=5)
    app.resize_button = tk.Button(
        resize_frame,
        text="Resize",
        width=10,
        command=app.operations.resize_image,
    )
    app.resize_button.pack(side=tk.LEFT, padx=5)

    # Rotate angle input box and button
    rotate_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    rotate_frame.pack(anchor="w", pady=5)
    app.rotate_input = tk.Entry(
        rotate_frame,
        textvariable=app.rotate_angle,
        width=10,
    )
    app.rotate_input.pack(side=tk.LEFT, padx=5)
    app.rotate_button = tk.Button(
        rotate_frame,
        text="Rotate",
        width=10,
        command=app.operations.rotate_image,
    )
    app.rotate_button.pack(side=tk.LEFT, padx=5)

def _setup_gray_level_slicing_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for gray level slicing.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Gray Level Slicing",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Preserve original values checkbox
    preserve_original_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    preserve_original_frame.pack(anchor="w", pady=5)
    app.preserve_original_checkbox = tk.Checkbutton(
        preserve_original_frame,
        text="Preserve Original",
        variable=app.preserve_original,
        onvalue=True,
        offvalue=False,
    )
    app.preserve_original_checkbox.pack(side=tk.LEFT, padx=5)

    # Buttons for applying gray level slicing changes
    app.slice_button = tk.Button(
        preserve_original_frame,
        text="Apply",
        width=10,
        command=app.operations.apply_gray_level_slicing,
    )
    app.slice_button.pack(side=tk.LEFT, padx=5)

    # Frame for min level label and input box
    min_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    min_frame.pack(anchor="w", pady=5)
    min_label = tk.Label(min_frame, text="Min Gray Level", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    min_label.pack(side=tk.LEFT, padx=5)
    app.min_gray_input = tk.Entry(
        min_frame,
        textvariable=app.min_gray,
        width=10,
    )
    app.min_gray_input.pack(side=tk.LEFT, padx=5)

    # Frame for max level label and input box
    max_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    max_frame.pack(anchor="w", pady=5)
    max_label = tk.Label(max_frame, text="Max Gray Level", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    max_label.pack(side=tk.LEFT, padx=5)
    app.max_gray_input = tk.Entry(
        max_frame,
        textvariable=app.max_gray,
        width=10,
    )
    app.max_gray_input.pack(side=tk.LEFT, padx=5)

def _setup_histogram_equalization_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for histogram equalization.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Histogram Equalization",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Button for histogram equalization
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    button_label = tk.Label(button_frame, text="Histogram Equalization", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    button_label.pack(side=tk.LEFT, padx=5)
    button_frame.pack(anchor="w", pady=5)
    app.equalize_button = tk.Button(
        button_frame,
        text="Apply",
        width=10,
        command=app.operations.equalize_histogram,
    )
    app.equalize_button.pack(side=tk.LEFT, padx=5)

def _setup_bit_plane_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for bit-plane images.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Bit-Plane Images",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Scale for selecting the bit-plane image
    scale_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    scale_frame.pack(anchor="w", pady=5)
    app.bit_plane_scale = tk.Scale(
        scale_frame,
        from_=0,
        to=7,
        orient=tk.HORIZONTAL,
        variable=app.bit_plane_level,
    )
    app.bit_plane_scale.pack(side=tk.LEFT, padx=5)

    # Button for displaying the bit-plane image
    app.bit_plane_button = tk.Button(
        scale_frame,
        text="Apply",
        width=10,
        command=app.operations.display_bit_plane_image,
    )
    app.bit_plane_button.pack(side=tk.LEFT, padx=5)

def _setup_smoothing_sharpening_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for smoothing and sharpening.
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Smoothing and Sharpening",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.pack(anchor="w", pady=5)

    # Smoothing label and input box
    smoothing_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    smoothing_frame.pack(anchor="w", pady=5)
    app.smoothing_input = tk.Entry(
        smoothing_frame,
        textvariable=app.smoothing_level,
        width=10,
    )
    app.smoothing_input.pack(side=tk.LEFT, padx=5)
    app.smoothing_button = tk.Button(
        smoothing_frame,
        text="Smooth",
        width=10,
        command=app.operations.smooth_image,
    )
    app.smoothing_button.pack(side=tk.LEFT, padx=5)

    # Sharpening label and input box
    sharpening_frame = tk.Frame(parent_frame, bg=MAIN_THEME)
    sharpening_frame.pack(anchor="w", pady=5)
    app.sharpening_input = tk.Entry(
        sharpening_frame,
        textvariable=app.sharpening_level,
        width=10,
    )
    app.sharpening_input.pack(side=tk.LEFT, padx=5)
    app.sharpening_button = tk.Button(
        sharpening_frame,
        text="Sharpen",
        width=10,
        command=app.operations.sharpen_image,
    )
    app.sharpening_button.pack(side=tk.LEFT, padx=5)
