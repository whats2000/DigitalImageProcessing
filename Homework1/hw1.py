"""
Construct a simple image processing tool with a graphic user interface (GUI),
providing the following functionalities:
1. Open/save/display 256-gray-level images in the format of JPG/TIF.
2. Adjust the contrast/brightness of images by changing the values of “a”
and “b” in 3 different methods:
(A) linearly (Y = aX +b);
(B) exponentially (Y = exp(aX+b));
(C) logarithmically (Y = ln(aX+b), b > 1).
3. Zoom in and shrink with respect to the images' original size by using
bilinear interpolation.
4. Rotate images by user-defined degrees.
5. Gray-level slicing: display images from a certain range of gray levels given
by users. 
Requirements: 
(1) users can define the range of gray levels to
be displayed; 
(2) users can choose either preserve the original values of unselected areas or 
display them as black color.
6. Display the histogram of images. An “auto-level” function by using histogram 
equalization should be provided.
7. Bit-Plane images: display the bit-plane images for the input image.
Requirements: users should be able to select which bit-plane image to be
displayed.
8. Smoothing and sharpening: providing smoothing and sharpening options
for the input images by using spatial filters. Requirements: the levels of
smoothing and sharpening should be defined by users via GUI.
"""
# First step is import the required libraries
import math
from typing import Union

import tkinter as tk
from tkinter import filedialog

import numpy as np
from PIL import Image, ImageTk

# Define the style for the application
MAIN_THEME = "#282c34"
MAIN_FONT_COLOR = "#ffffff"
MAIN_ACTIVE_COLOR = "#528bff"


class ImageProcessorCore:
    @staticmethod
    def adjust_brightness(image: Image.Image, alpha: float, beta: float, algorithm: str) -> Image.Image:
        """
        Adjust the brightness of an image using a linear, exponential, or logarithmic algorithm
        Args:
            image: The image to adjust
            alpha: The alpha value for the algorithm
            beta: The beta value for the algorithm
            algorithm: The algorithm to use for adjusting the brightness
        Returns:
            The adjusted image
        """
        image_array = np.array(image)

        if beta <= 1 and algorithm == "Logarithmic":
            raise ValueError("Beta value must be greater than 1 for logarithmic algorithm")

        if algorithm == "Linear":
            new_image = alpha * image_array + beta
        elif algorithm == "Exponential":
            new_image = np.exp(alpha * image_array + beta)
        elif algorithm == "Logarithmic":
            new_image = np.log(alpha * image_array + beta)
        else:
            raise ValueError("Invalid brightness algorithm")

        # Clip the values to 0-255
        new_image = np.clip(new_image, 0, 255)

        return Image.fromarray(new_image)


class ImageProcessorApp:
    def __init__(self, root_window: tk.Tk):
        """
        Initialize the ImageProcessorApp
        Args:
            root_window: The root window of the application
        """
        self.root = root_window
        self.root.title('Image Processor Tool')

        # Attributes for the image processing
        self.image: Union[Image.Image, None] = None
        self.brightness_alpha = tk.DoubleVar()
        self.brightness_alpha.set(1.0)
        self.brightness_beta = tk.DoubleVar()
        self.brightness_algorithm = tk.StringVar()
        self.brightness_algorithm.set("Linear")

        # Set up the window
        self._setup_window()
        # Set up the main image display frame
        self._setup_image_display_frame()
        # Set up the right operations frame
        right_operations_frame = tk.Frame(self.root, bg=MAIN_THEME)
        right_operations_frame.grid(row=0, column=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self._setup_upload_download_frame(right_operations_frame)
        self._setup_contrast_brightness_frame(right_operations_frame)

    def _setup_window(self):
        """
        Set up the window size and make it resizable
        """
        # Get the screen width and height multiplied by 0.5 as the default window size
        window_width = math.floor(root.winfo_screenwidth() * 0.5)
        window_height = math.floor(root.winfo_screenheight() * 0.5)

        # Set the window size
        self.root.geometry(f"{window_width}x{window_height}")

        # Make screen resizable
        self.root.resizable(True, True)

    def _setup_image_display_frame(self):
        """
        Set up the frame for displaying the image
        """
        # Create a frame to hold the image
        image_frame = tk.Frame(self.root, bg=MAIN_THEME, pady=10)
        image_frame.grid(row=0, column=0)

        # Center the frame horizontally (X-axis) using column configuration
        self.root.grid_columnconfigure(0, weight=1)

        # Display the image using a label
        self.image_label = tk.Label(image_frame, bg=MAIN_THEME)
        self.image_label.pack()

    def _setup_upload_download_frame(self, parent_frame: tk.Frame):
        """
        Set up the frame for uploading and downloading images
        """
        # Create a frame to hold the buttons
        button_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
        button_frame.grid(row=0, column=0)

        # Center the frame horizontally (X-axis) using column configuration
        self.root.grid_columnconfigure(0, weight=1)

        # Buttons for opening and saving images
        self.open_button = tk.Button(
            button_frame,
            text="Open Image",
            command=self._open_image,
        )
        self.save_button = tk.Button(
            button_frame,
            text="Save Image",
            command=self._save_image,
        )

        self.open_button.pack(side=tk.LEFT, padx=10)
        self.save_button.pack(side=tk.LEFT, padx=10)

    def _setup_contrast_brightness_frame(self, parent_frame: tk.Frame):
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
        selection_text.grid(row=1, column=0)

        # Menu for selecting the brightness algorithm
        menu_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
        menu_frame.grid(row=2, column=0)
        self.brightness_menu = tk.OptionMenu(
            menu_frame,
            self.brightness_algorithm,
            "Linear",
            "Exponential",
            "Logarithmic",
        )
        self.brightness_apply_button = tk.Button(
            menu_frame,
            text="Apply",
            command=self._apply_brightness_algorithm,
        )
        self.brightness_menu.pack(side=tk.LEFT, padx=10)
        self.brightness_apply_button.pack(side=tk.LEFT, padx=10)

        # Input boxes for adjusting alpha and beta values
        input_boxes_frame = tk.Frame(parent_frame, bg=MAIN_THEME, pady=10)
        input_boxes_frame.grid(row=3, column=0)
        self.alpha_input = tk.Entry(
            input_boxes_frame,
            textvariable=self.brightness_alpha,
            width=10,
        )
        self.beta_input = tk.Entry(
            input_boxes_frame,
            textvariable=self.brightness_beta,
            width=10,
        )

        self.alpha_input.pack(side=tk.LEFT, padx=10)
        self.beta_input.pack(side=tk.LEFT, padx=10)

    def _open_image(self):
        """
        Open an image from the file dialog
        """
        file_path = filedialog.askopenfilename()

        # Prevent illegal file path
        if not file_path:
            return

        # Update the image label with the new image
        self._update_image(Image.open(file_path))

    def _save_image(self):
        """
        Save the image to a file
        """
        file_name = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
        )

        # Only save the image if the file name is not empty and the image is exist
        if not file_name or not self.image:
            return
        image_to_save = self.image.convert("RGB")
        image_to_save.save(file_name)

    def _update_image(self, new_image: Image.Image):
        """
        Update the image label with a new image
        Args:
            new_image: The new image to display
        """
        self.image = new_image
        photo_image = ImageTk.PhotoImage(new_image)
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image

    def _apply_brightness_algorithm(self):
        """
        Apply the brightness algorithm to a pixel value
        """
        algorithm = self.brightness_algorithm.get()
        alpha = self.brightness_alpha.get()
        beta = self.brightness_beta.get()

        # Apply the brightness algorithm to the image
        new_image = ImageProcessorCore.adjust_brightness(self.image, alpha, beta, algorithm)

        # Update the image
        self._update_image(new_image)


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.configure(background=MAIN_THEME)
    root.mainloop()
