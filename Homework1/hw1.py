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
from PIL import Image, ImageTk

# Define the style for the application
MAIN_THEME = "#282c34"
MAIN_FONT_COLOR = "#ffffff"
MAIN_ACTIVE_COLOR = "#528bff"
BUTTON_STYLE = {
    "bg": MAIN_THEME,
    "fg": MAIN_FONT_COLOR,
    "activebackground": MAIN_ACTIVE_COLOR,
    "activeforeground": MAIN_FONT_COLOR,
}


class ImageProcessorApp:
    def __init__(self, root_window: tk.Tk):
        """
        Initialize the ImageProcessorApp
        Args:
            root_window: The root window of the application
        """
        self.root = root_window
        self.root.title('Image Processor Tool')

        # Attributes for the image
        self.image: Union[Image.Image, None] = None

        # Set up the app
        self._setup_window()
        self._setup_image_display_frame()
        self._setup_upload_download_frame()

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

    def _setup_upload_download_frame(self):
        """
        Set up the frame for uploading and downloading images
        """
        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root, bg=MAIN_THEME, pady=10)
        button_frame.grid(row=1, column=0)

        # Center the frame horizontally (X-axis) using column configuration
        self.root.grid_columnconfigure(0, weight=1)

        # Buttons for opening and saving images
        self.open_button = tk.Button(
            button_frame,
            text="Open Image",
            command=self.open_image,
            **BUTTON_STYLE
        )
        self.save_button = tk.Button(
            button_frame,
            text="Save Image",
            command=self.save_image,
            **BUTTON_STYLE
        )

        # Pack the buttons side by side within the frame (with some padding)
        self.open_button.pack(side=tk.LEFT, padx=10)
        self.save_button.pack(side=tk.LEFT, padx=10)

    def open_image(self):
        """
        Open an image from the file dialog
        """
        file_path = filedialog.askopenfilename()

        # Prevent illegal file path
        if not file_path:
            return

        # Read the image using PIL
        self.image = Image.open(file_path)

        # Convert the image to ImageTk.PhotoImage
        photo_image = ImageTk.PhotoImage(self.image)

        # Update the image label
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image

    def save_image(self):
        """
        Save the image to a file
        """
        file_name = filedialog.asksaveasfilename(defaultextension=".jpg")

        # Only save the image if the file name is not empty and the image is exist
        if not file_name or not self.image:
            return

        self.image.save(file_name)


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.configure(background=MAIN_THEME)
    root.mainloop()
