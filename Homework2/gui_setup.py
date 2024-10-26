import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR
from utils import open_image, save_image

if TYPE_CHECKING:
    from app import ImageProcessorApp


def setup_gui(app: 'ImageProcessorApp'):
    """
    Set up the GUI for the image processor tool
    """
    # Set up window
    _setup_window(app)

    # Set up the main image display frame
    left_display_frame = tk.Frame(app.root, bg=MAIN_THEME)
    left_display_frame.grid(row=0, column=0)
    _setup_image_display_frame(app, left_display_frame)

    # Set up the right operations frame
    right_operations_frame = tk.Frame(app.root, bg=MAIN_THEME)
    right_operations_frame.grid(row=0, column=1)
    app.root.grid_columnconfigure(1, weight=1)
    app.root.grid_rowconfigure(0, weight=1)
    _setup_upload_download_frame(app, right_operations_frame)
    _setup_contrast_brightness_frame(app, right_operations_frame)
    _setup_resize_rotate_frame(app, right_operations_frame)
    _setup_gray_level_slicing_frame(app, right_operations_frame)
    _setup_histogram_equalization_frame(app, right_operations_frame)
    _setup_bit_plane_frame(app, right_operations_frame)
    _setup_smoothing_sharpening_frame(app, right_operations_frame)



def _setup_window(app: 'ImageProcessorApp'):
    """
    Set up the window size and make it resizable
    """
    # Get the screen width and height multiplied by 0.5 as the default window size
    window_width = int(app.root.winfo_screenwidth() * 0.5)
    window_height = int(app.root.winfo_screenheight() * 0.5)

    # Set the window size
    app.root.geometry(f"{window_width}x{window_height}")

    # Make the window resizable
    app.root.resizable(True, True)


def _setup_image_display_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for displaying the image
    """
    # Center the frame
    app.root.grid_columnconfigure(0, weight=1)
    app.root.grid_rowconfigure(0, weight=1)

    # Create a frame to hold the image
    title = tk.Label(parent_frame, text="Image Display", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    title.grid(row=0, column=0)
    image_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    image_frame.grid(row=1, column=0)

    # Create a frame for histogram
    title = tk.Label(parent_frame, text="Histogram", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    title.grid(row=0, column=1)
    histogram_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    histogram_frame.grid(row=1, column=1)

    # Display the image using a label
    app.image_label = tk.Label(image_frame, bg=MAIN_THEME)
    app.image_label.pack()

    # Display the histogram using a label
    app.histogram_label = tk.Label(histogram_frame, bg=MAIN_THEME)
    app.histogram_label.pack()

    # Undo and redo buttons
    undo_button = tk.Button(parent_frame, text="Undo", command=app.undo_image)
    redo_button = tk.Button(parent_frame, text="Redo", command=app.redo_image)
    undo_button.grid(row=2, column=0)
    redo_button.grid(row=2, column=1)


def _setup_upload_download_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame):
    """
    Set up the frame for uploading and downloading images
    """
    # Create a frame to hold the buttons
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.grid(row=0, column=0)

    # Center the frame horizontally (X-axis) using column configuration
    app.root.grid_columnconfigure(0, weight=1)

    # Buttons for opening and saving images
    app.open_button = tk.Button(
        button_frame,
        text="Open Image",
        command=lambda: open_image(app),
    )
    app.save_button = tk.Button(
        button_frame,
        text="Save Image",
        command=lambda: save_image(app),
    )

    app.open_button.pack(side=tk.LEFT, padx=10)
    app.save_button.pack(side=tk.LEFT, padx=10)

def _setup_contrast_brightness_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=1):
    """
    Set up the frame for adjusting alpha and beta values for brightness/contrast
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Adjust brightness and contrast",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Menu for selecting the brightness algorithm
    menu_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    menu_frame.grid(row=start_row + 1, column=0)
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
    app.brightness_menu.pack(side=tk.LEFT, padx=10)
    app.brightness_apply_button.pack(side=tk.LEFT, padx=10)

    # Alpha frame for adjusting
    alpha_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    alpha_frame.grid(row=start_row + 2, column=0)
    alpha_label = tk.Label(alpha_frame, text="a value", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.alpha_input = tk.Entry(
        alpha_frame,
        textvariable=app.brightness_alpha,
        width=10,
    )
    alpha_label.pack(side=tk.LEFT, padx=10)
    app.alpha_input.pack(side=tk.LEFT, padx=10)

    # Beta frame for adjusting
    beta_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    beta_frame.grid(row=start_row + 3, column=0)
    beta_label = tk.Label(beta_frame, text="b value", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.beta_input = tk.Entry(
        beta_frame,
        textvariable=app.brightness_beta,
        width=10,
    )
    beta_label.pack(side=tk.LEFT, padx=10)
    app.beta_input.pack(side=tk.LEFT, padx=10)

def _setup_resize_rotate_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=5):
    """
    Set up the frame for resizing and rotating images
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Resize and Rotate",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Resize scale input box and button
    resize_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    resize_frame.grid(row=start_row + 1, column=0)
    app.resize_input = tk.Entry(
        resize_frame,
        textvariable=app.resize_scale,
        width=10,
    )

    app.resize_input.pack(side=tk.LEFT, padx=10)
    app.resize_button = tk.Button(
        resize_frame,
        text="Resize",
        width=10,
        command=app.operations.resize_image,
    )
    app.resize_button.pack(side=tk.LEFT, padx=10)

    # Rotate angle input box and button
    rotate_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    rotate_frame.grid(row=start_row + 2, column=0)
    app.rotate_input = tk.Entry(
        rotate_frame,
        textvariable=app.rotate_angle,
        width=10,
    )
    app.rotate_button = tk.Button(
        rotate_frame,
        text="Rotate",
        width=10,
        command=app.operations.rotate_image,
    )
    app.rotate_input.pack(side=tk.LEFT, padx=10)
    app.rotate_button.pack(side=tk.LEFT, padx=10)

def _setup_gray_level_slicing_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=8):
    """
    Set up the frame for gray level slicing
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Gray Level Slicing",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Preserve original values checkbox
    preserve_original_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    preserve_original_frame.grid(row=start_row + 1, column=0)
    app.preserve_original_checkbox = tk.Checkbutton(
        preserve_original_frame,
        text="Preserve Original",
        variable=app.preserve_original,
        onvalue=True,
        offvalue=False,
    )
    app.preserve_original_checkbox.pack(side=tk.LEFT, padx=10)

    # Buttons for applying gray level slicing changes
    app.slice_button = tk.Button(
        preserve_original_frame,
        text="Apply",
        width=10,
        command=app.operations.apply_gray_level_slicing,
    )
    app.slice_button.pack(side=tk.LEFT, padx=10)

    # Frame for min level label and input box
    min_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    min_frame.grid(row=start_row + 2, column=0)
    min_label = tk.Label(min_frame, text="Min Gray Level", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.min_gray_input = tk.Entry(
        min_frame,
        textvariable=app.min_gray,
        width=10,
    )
    min_label.pack(side=tk.LEFT, padx=10)
    app.min_gray_input.pack(side=tk.LEFT, padx=10)

    # Frame for max level label and input box
    max_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    max_frame.grid(row=start_row + 3, column=0)
    max_label = tk.Label(max_frame, text="Max Gray Level", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    app.max_gray_input = tk.Entry(
        max_frame,
        textvariable=app.max_gray,
        width=10,
    )
    max_label.pack(side=tk.LEFT, padx=10)
    app.max_gray_input.pack(side=tk.LEFT, padx=10)

def _setup_histogram_equalization_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=13):
    """
    Set up the frame for histogram equalization
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Histogram Equalization",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Button for histogram equalization
    button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    button_frame.grid(row=start_row + 1, column=0)
    app.equalize_button = tk.Button(
        button_frame,
        text="Equalize",
        width=10,
        command=app.operations.equalize_histogram,
    )

    app.equalize_button.pack(side=tk.LEFT, padx=10)

def _setup_bit_plane_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=15):
    """
    Set up the frame for bit-plane images
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Bit-Plane Images",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Scale for selecting the bit-plane image
    scale_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    scale_frame.grid(row=start_row + 1, column=0)
    app.bit_plane_scale = tk.Scale(
        scale_frame,
        from_=0,
        to=7,
        orient=tk.HORIZONTAL,
        variable=app.bit_plane_level,
    )
    app.bit_plane_scale.pack(side=tk.LEFT, padx=10)

    # Button for displaying the bit-plane image
    app.bit_plane_button = tk.Button(
        scale_frame,
        text="Apply",
        width=10,
        command=app.operations.display_bit_plane_image,
    )
    app.bit_plane_button.pack(side=tk.LEFT, padx=10)

def _setup_smoothing_sharpening_frame(app: 'ImageProcessorApp', parent_frame: tk.Frame, start_row=17):
    """
    Set up the frame for smoothing and sharpening
    """
    # Selection Text
    selection_text = tk.Label(
        parent_frame,
        text="Smoothing and Sharpening",
        bg=MAIN_THEME,
        fg=MAIN_FONT_COLOR,
    )
    selection_text.grid(row=start_row, column=0)

    # Smoothing label and input box
    smoothing_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    smoothing_frame.grid(row=start_row + 1, column=0)
    app.smoothing_input = tk.Entry(
        smoothing_frame,
        textvariable=app.smoothing_level,
        width=10,
    )
    app.smoothing_button = tk.Button(
        smoothing_frame,
        text="Smooth",
        width=10,
        command=app.operations.smooth_image,
    )
    app.smoothing_input.pack(side=tk.LEFT, padx=10)
    app.smoothing_button.pack(side=tk.LEFT, padx=10)

    # Sharpening label and input box
    sharpening_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    sharpening_frame.grid(row=start_row + 2, column=0)
    app.sharpening_input = tk.Entry(
        sharpening_frame,
        textvariable=app.sharpening_level,
        width=10,
    )
    app.sharpening_button = tk.Button(
        sharpening_frame,
        text="Sharpen",
        width=10,
        command=app.operations.sharpen_image,
    )
    app.sharpening_input.pack(side=tk.LEFT, padx=10)
    app.sharpening_button.pack(side=tk.LEFT, padx=10)
