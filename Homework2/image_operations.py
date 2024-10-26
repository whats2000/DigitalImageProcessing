from tkinter import messagebox
from typing import TYPE_CHECKING

from image_processor_core import ImageProcessorCore

if TYPE_CHECKING:
    from app import ImageProcessorApp

class ImageOperations:
    def __init__(self, app: 'ImageProcessorApp'):
        self.app = app

    def apply_brightness_algorithm(self):
        """
        Apply the brightness algorithm to a pixel value
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        algorithm = self.app.brightness_algorithm.get()
        alpha = self.app.brightness_alpha.get()
        beta = self.app.brightness_beta.get()

        # Apply the brightness algorithm to the image
        new_image = ImageProcessorCore.adjust_brightness(self.app.image, alpha, beta, algorithm)

        # Update the image
        self.app.update_image(new_image)

    def resize_image(self):
        """
        Resize the image using the scale factor
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        scale_factor = self.app.resize_scale.get()

        # Resize the image
        new_image = ImageProcessorCore.resize_image(self.app.image, scale_factor)

        # Update the image
        self.app.update_image(new_image)

    def rotate_image(self):
        """
        Rotate the image using the angle
        """
        if not self.app.image:
            return

        angle = self.app.rotate_angle.get()

        # Rotate the image
        new_image = ImageProcessorCore.rotate_image(self.app.image, angle)

        # Update the image
        self.app.update_image(new_image)

    def apply_gray_level_slicing(self):
        """
        Apply gray level slicing to the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        min_gray = self.app.min_gray.get()
        max_gray = self.app.max_gray.get()
        preserve_original = self.app.preserve_original.get()

        if min_gray > max_gray:
            messagebox.showinfo("Info", "Min gray level must be less than max gray level")
            return

        # Apply gray-level slicing
        sliced_image = ImageProcessorCore.gray_level_slicing(self.app.image, min_gray, max_gray, preserve_original)

        self.app.update_image(sliced_image)

    def equalize_histogram(self):
        """
        Equalize the histogram of the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        # Equalize the histogram
        new_image = ImageProcessorCore.histogram_equalization(self.app.image)

        # Update the image
        self.app.update_image(new_image)

    def display_bit_plane_image(self):
        """
        Display the bit-plane image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        bit_plane = self.app.bit_plane_level.get()

        if bit_plane < 0 or bit_plane > 7:
            messagebox.showinfo("Info", "Bit-plane level must be between 0 and 7")
            return

        new_image = ImageProcessorCore.bit_plane_image(self.app.image, bit_plane)
        self.app.update_image(new_image)

    def smooth_image(self):
        """
        Smooth the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        smoothing_level = self.app.smoothing_level.get()

        # Smooth the image
        new_image = ImageProcessorCore.smooth_image(self.app.image, smoothing_level)

        # Update the image
        self.app.update_image(new_image)

    def sharpen_image(self):
        """
        Sharpen the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        sharpening_level = self.app.sharpening_level.get()

        # Sharpen the image
        new_image = ImageProcessorCore.sharpen_image(self.app.image, sharpening_level)

        # Update the image
        self.app.update_image(new_image)
