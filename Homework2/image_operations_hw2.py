from tkinter import messagebox
from typing import TYPE_CHECKING

import numpy as np
from PIL import Image

from image_operations_hw1 import ImageOperationsHW1
from image_processor_core_hw2 import ImageProcessorCore2

if TYPE_CHECKING:
    from app import ImageProcessorApp


class ImageOperationsHW2(ImageOperationsHW1):
    def __init__(self, app: 'ImageProcessorApp'):
        super().__init__(app)
        self.app = app

    def apply_averaging_mask(self, mask_size: int = 3):
        """
        Apply an averaging mask to both the main and comparison images using OpenCV.

        Args:
            mask_size (int): The size of the averaging mask
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore2.apply_average_mask(self.app.image, mask_size)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore2.apply_average_mask(self.app.compare_image, mask_size)
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

        main_filtered_image = ImageProcessorCore2.apply_median_mask(self.app.image, mask_size)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore2.apply_median_mask(self.app.compare_image, mask_size)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_laplacian_mask(self):
        """
        Apply a Laplacian mask to the main image and, if present, the comparison image using OpenCV.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore2.apply_laplacian_mask(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore2.apply_laplacian_mask(self.app.compare_image)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_fft(self):
        """
        Apply the Fast Fourier Transform (FFT) to the main image and, if present, the comparison image.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        # Compute FFT on the main image
        main_fft_image = ImageProcessorCore2.apply_fft(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_fft_image, None])
            return

        # Compute FFT on the comparison image
        compare_fft_image = ImageProcessorCore2.apply_fft(self.app.compare_image)
        self.app.update_image([main_fft_image, compare_fft_image])

    def apply_inverse_fft_magnitude_only(self):
        """
        Apply the Inverse Fast Fourier Transform (FFT) to the main image and, if present, the comparison image.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        # Compute FFT on the main image
        main_fft_image = ImageProcessorCore2.inverse_fft_magnitude_only(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_fft_image, None])
            return

        # Compute FFT on the comparison image
        compare_fft_image = ImageProcessorCore2.inverse_fft_magnitude_only(self.app.compare_image)
        self.app.update_image([main_fft_image, compare_fft_image])

    def apply_inverse_fft_phase_only(self):
        """
        Apply the Inverse Fast Fourier Transform (FFT) to the main image and, if present, the comparison image.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        # Compute FFT on the main image
        main_fft_image = ImageProcessorCore2.inverse_fft_phase_only(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_fft_image, None])
            return

        # Compute FFT on the comparison image
        compare_fft_image = ImageProcessorCore2.inverse_fft_phase_only(self.app.compare_image)
        self.app.update_image([main_fft_image, compare_fft_image])

    def multiply_by_neg_1(self):
        """
        Step 1: Multiply the image by (-1)^(x+y)
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        image_array = np.array(self.app.image)
        main_filtered_array = ImageProcessorCore2.multiply_by_neg_1(image_array)
        main_filtered_image = Image.fromarray(main_filtered_array.astype(np.uint8))
        self.app.temp_array = main_filtered_array
        self.app.update_image([main_filtered_image, None])

    def compute_dft(self):
        """
        Step 2: Compute the DFT and return the magnitude spectrum.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        if self.app.temp_array is None:
            self.app.temp_array = np.array(self.app.image)

        main_fft_array = ImageProcessorCore2.compute_dft(self.app.temp_array)
        main_filtered_image = Image.fromarray(main_fft_array.real.astype(np.uint8))
        self.app.temp_array = main_fft_array
        self.app.update_image([main_filtered_image, None])

    def take_conjugate(self):
        """
        Step 3: Compute the DFT and return the magnitude spectrum of the conjugate.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        if self.app.temp_array is None:
            self.app.temp_array = np.array(self.app.image)

        main_conjugate_array = ImageProcessorCore2.take_conjugate(self.app.temp_array)
        main_filtered_image = Image.fromarray(
            (np.abs(main_conjugate_array) / np.max(np.abs(main_conjugate_array)) * 255).astype(np.uint8)
        )
        self.app.temp_array = main_conjugate_array
        self.app.update_image([main_filtered_image, None])

    def compute_inverse_dft(self):
        """
        Step 4: Compute the inverse DFT.
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        if self.app.temp_array is None:
            self.app.temp_array = np.array(self.app.image)

        main_inverse_dft = ImageProcessorCore2.compute_inverse_dft(self.app.temp_array)
        main_filtered_image = Image.fromarray(main_inverse_dft.real.astype(np.uint8))
        self.app.temp_array = main_inverse_dft
        self.app.update_image([main_filtered_image, None])

    def multiply_by_neg_1_final(self):
        """
        Step 5: Multiply the real part of the result by (-1)^(x+y)
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        if self.app.temp_array is None:
            self.app.temp_array = np.array(self.app.image)

        main_filtered_array = ImageProcessorCore2.multiply_by_neg_1(self.app.temp_array)
        main_filtered_image = Image.fromarray(main_filtered_array.real.astype(np.uint8))
        self.app.temp_array = main_filtered_array
        self.app.update_image([main_filtered_image, None])