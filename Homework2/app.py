import tkinter as tk
from tkinter import messagebox
from typing import Union, List, Any

import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

from gui_setup import setup_gui
from image_operations_hw2 import ImageOperationsHW2


class ImageProcessorApp:
    def __init__(self, root_window: tk.Tk):
        self.root = root_window
        self.root.title('Image Processor Tool')

        # Attributes for the image processing
        self.image: Union[Image.Image, None] = None
        self.compare_image: Union[Image.Image, None] = None
        self.image_label: Union[tk.Label, None] = None
        self.histogram_compare_label: Union[tk.Label, None] = None
        self.image_history: List[List[Image.Image]] = []
        self.redo_stack: List[List[Image.Image]] = []
        self.brightness_alpha = tk.DoubleVar()
        self.brightness_alpha.set(1.0)
        self.brightness_beta = tk.DoubleVar()
        self.brightness_algorithm = tk.StringVar()
        self.brightness_algorithm.set("Linear")
        self.resize_scale = tk.DoubleVar()
        self.resize_scale.set(1.0)
        self.rotate_angle = tk.DoubleVar()
        self.rotate_angle.set(0.0)
        self.min_gray = tk.IntVar()
        self.min_gray.set(0)
        self.max_gray = tk.IntVar()
        self.max_gray.set(255)
        self.preserve_original = tk.BooleanVar()
        self.preserve_original.set(True)
        self.bit_plane_level = tk.IntVar()
        self.bit_plane_level.set(0)
        self.smoothing_level = tk.IntVar()
        self.smoothing_level.set(1)
        self.sharpening_level = tk.IntVar()
        self.sharpening_level.set(1)

        # Set up operations
        self.operations = ImageOperationsHW2(self)

        # GUI setup
        setup_gui(self)

    def undo_image(self):
        """
        Undo the last image change
        """
        if not self.image_history:
            messagebox.showinfo("Info", "No more actions to undo")
            return

        # Push the current image to the redo stack
        self.redo_stack.append([self.image, self.compare_image])

        # Pop the last image from history and update
        previous_image = self.image_history.pop()
        self.update_image(previous_image, append_history=False)

    def redo_image(self):
        """
        Redo the last image change
        """
        if not self.redo_stack:
            messagebox.showinfo("Info", "No more actions to redo")
            return

            # Push the current image back to the history stack
        self.image_history.append([self.image, self.compare_image])

        # Pop the last image from the redo stack and update
        next_image = self.redo_stack.pop()
        self.update_image(next_image, append_history=False)


    def update_image(self, new_images: List[Image.Image], append_history: bool = True):
        """
        Update the image label with a new image
        Args:
            new_images: The new images to display
            append_history: Whether to append the current image to the history
        """
        if append_history:
            # Append current image to history before updating
            if self.image is not None:
                self.image_history.append([self.image, self.compare_image])

            if len(new_images) == 1 or new_images[1] is None:
                self.compare_image = None

            # Clear the redo stack when a new image operation is performed
            self.redo_stack.clear()

            # Keep history size reasonable
            if len(self.image_history) > 10:
                self.image_history.pop(0)

        self.image = new_images[0]
        photo_image: Any = ImageTk.PhotoImage(new_images[0])
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image
        if new_images[1] is not None:
            self.compare_image = new_images[1]
            photo_image: Any = ImageTk.PhotoImage(new_images[1])
            self.histogram_compare_label.config(image=photo_image)
            self.histogram_compare_label.image = photo_image
        else:
            self.update_histogram()

    def update_histogram(self):
        """
        Update the histogram of the image
        """
        # Update the histogram
        image_array = np.array(self.image)
        plt.figure("Histogram")
        plt.clf()
        plt.hist(image_array.flatten(), bins=256, range=(0, 255), color='gray', alpha=0.7)
        plt.title("Image Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.grid()
        plt.savefig("histogram.png", dpi=100)
        histogram_image = Image.open("histogram.png").resize(
            (min(400, self.image.width), min(400, self.image.height))
        )
        histogram_photo_image: Any = ImageTk.PhotoImage(histogram_image)
        self.histogram_compare_label.config(image=histogram_photo_image)
        self.histogram_compare_label.image = histogram_photo_image
