import tkinter as tk
from typing import TYPE_CHECKING

from config import MAIN_THEME, MAIN_FONT_COLOR, SECONDARY_THEME
from panel_swapper import PanelSwapper
from utils import open_image, save_image

if TYPE_CHECKING:
    from app import ImageProcessorApp

def setup_gui(app):
    """
    Set up the main layout for the GUI.
    """
    _setup_window(app)

    # Set up left image display frame
    left_display_frame = tk.Frame(app.root, bg=MAIN_THEME)
    left_display_frame.grid(row=0, column=0, rowspan=1)
    _setup_image_display_frame(app, left_display_frame)

    # Set up right operation panel
    right_operation_frame = tk.Frame(app.root, bg=MAIN_THEME)
    right_operation_frame.grid(row=0, column=1, rowspan=1)

    # Set up file upload/download frame
    upload_download_frame = tk.Frame(right_operation_frame, bg=MAIN_THEME)
    upload_download_frame.grid(row=0, column=1, sticky="nw")
    _setup_upload_download_frame(app, upload_download_frame)

    # Initialize the panel swapper for HW1 and HW2
    operation_panel_container = tk.Frame(right_operation_frame, bg=MAIN_THEME)
    operation_panel_container.grid(row=1, column=1, sticky="nsew")
    app.panel_swapper = PanelSwapper(app, operation_panel_container)
    app.panel_swapper.show_panel("HW3")


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
    title = tk.Label(parent_frame, text="Histogram/Comparison Image", bg=MAIN_THEME, fg=MAIN_FONT_COLOR)
    title.grid(row=0, column=1)
    histogram_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
    histogram_frame.grid(row=1, column=1)

    # Display the image using a label
    app.image_label = tk.Label(image_frame, bg=MAIN_THEME)
    app.image_label.pack()

    # Display the histogram using a label
    app.histogram_compare_label = tk.Label(histogram_frame, bg=MAIN_THEME)
    app.histogram_compare_label.pack()

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
    button_frame.grid(row=0, column=1)

    # Buttons for opening and saving images
    app.open_button = tk.Button(
        button_frame,
        fg=MAIN_FONT_COLOR,
        bg=SECONDARY_THEME,
        text="Open Image",
        command=lambda: open_image(app),
    )
    app.save_button = tk.Button(
        button_frame,
        fg=MAIN_FONT_COLOR,
        bg=SECONDARY_THEME,
        text="Save Image",
        command=lambda: save_image(app),
    )
    app.open_button.pack(side=tk.LEFT)
    app.save_button.pack(side=tk.LEFT, padx=10)
