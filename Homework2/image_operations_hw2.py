from tkinter import messagebox
from typing import TYPE_CHECKING

import numpy as np

from image_operations_hw1 import ImageOperationsHW1
from image_processor_core import ImageProcessorCore

if TYPE_CHECKING:
    from app import ImageProcessorApp


class ImageOperationsHW2(ImageOperationsHW1):
    def __init__(self, app: 'ImageProcessorApp'):
        super().__init__(app)
        self.app = app

    def apply_averaging_mask(self, mask_size: int = 3):
        """
        Apply a averaging mask to both the main and comparison images using OpenCV.

        Args:
            mask_size (int): The size of the averaging mask
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore.apply_average_mask(self.app.image, mask_size)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore.apply_average_mask(self.app.compare_image, mask_size)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_median_mask(self, mask_size: int = 3):
        """
        Apply a 3x3 median filter to both the main and comparison images using OpenCV.

        Args:
            mask_size (int): The size of the median mask
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore.apply_median_mask(self.app.image, mask_size)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore.apply_median_mask(self.app.compare_image, mask_size)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_laplacian_mask(self):
        """
        Apply a Laplacian mask to the main image and, if present, the comparison image using OpenCV.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore.apply_laplacian_mask(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore.apply_laplacian_mask(self.app.compare_image)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_fft(self):
        pass

    def apply_fft_magnitude_phase(self):
        pass

    def apply_fft_magnitude_only(self):
        pass

    def apply_fft_phase_only(self):
        pass
