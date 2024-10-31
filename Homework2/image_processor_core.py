import math
from tkinter import messagebox

import cv2
import numpy as np
from PIL import Image

# This is for working with the PIL library older
if not hasattr(Image, 'Resampling'):
    Image.Resampling = Image

USE_MANUALLY_FUNCTION = False


class ImageProcessorCore:
    @staticmethod
    def convolution(image_array: np.array, mask: np.array) -> np.array:
        """
        Convolve the image with the given mask
        Args:
            image_array: The image array to convolve
            mask: The mask to use for convolution
        Returns:
            The convolved image
        """
        width, height = image_array.shape[0], image_array.shape[1]
        mask_width, mask_height = mask.shape
        assert mask_width % 2 == 1 and mask_height % 2 == 1, "Mask dimensions must be odd"

        # Calculate the padding needed for the mask
        padding_width = mask_width // 2
        padding_height = mask_height // 2
        result_image = np.zeros((width, height), dtype=np.float32)

        # Pad the image with zeros
        padded_image = np.pad(
            image_array,
            ((padding_width, padding_width),
             (padding_height, padding_height)),
            mode='constant',
            constant_values=0
        )

        # Convolve the image with the mask
        for i in range(width):
            for j in range(height):
                # The region mask is the region of the image that the mask will be applied to
                region_mask = padded_image[
                                  i:i + mask_height,
                                  j:j + mask_width
                              ]
                # Apply the mask to the region
                result_image[i, j] = np.sum(region_mask * mask)

        return result_image.clip(0, 255).astype(np.uint8)

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
        image_array = np.array(image, dtype=np.float32)

        if beta <= 1 and algorithm == "Logarithmic":
            messagebox.showerror("Error", "Beta value must be greater than 1 for logarithmic algorithm")
            raise ValueError("Beta value must be greater than 1 for logarithmic algorithm")

        if algorithm == "Linear":
            new_image = alpha * image_array + beta
        elif algorithm == "Exponential":
            # Apply the exponential algorithm
            new_image = np.exp(alpha * image_array + beta)
            # Apply normalization to the logarithmic algorithm
            new_image = (new_image - np.min(new_image)) / (np.max(new_image) - np.min(new_image)) * 255
        elif algorithm == "Logarithmic":
            # Apply the logarithmic algorithm
            new_image = np.log(alpha * image_array + beta)
            # Apply normalization to the logarithmic algorithm
            new_image = (new_image - np.min(new_image)) / (np.max(new_image) - np.min(new_image)) * 255
        else:
            messagebox.showerror("Error", "Invalid brightness algorithm")
            raise ValueError("Invalid brightness algorithm")

        # Clip the values to 0-255
        new_image = np.clip(new_image, 0, 255)

        return Image.fromarray(new_image.astype(np.uint8))

    @staticmethod
    def resize_image(image: Image.Image, scale_factor: float) -> Image.Image:
        """
        Resize an image using bilinear interpolation
        Args:
            image: The image to resize
            scale_factor: The scale factor for resizing
        Returns:
            The resized image
        """
        # Use PIL's built-in resize function with bilinear interpolation
        return image.resize(
            (
                math.floor(image.width * scale_factor),
                math.floor(image.height * scale_factor)
            ),
            Image.Resampling.BILINEAR
        )

    @staticmethod
    def rotate_image(image: Image.Image, angle: float) -> Image.Image:
        """
        Rotate an image by a given angle
        Args:
            image: The image to rotate
            angle: The angle to rotate the image by
        Returns:
            The rotated image
        """
        # Use PIL's built-in rotate function with bilinear
        return image.rotate(angle, resample=Image.Resampling.BILINEAR)

    @staticmethod
    def gray_level_slicing(image: Image.Image, min_gray: int, max_gray: int, preserve_original: bool) -> Image.Image:
        """
        Perform gray level slicing on an image
        Args:
            image: The input image to apply gray level slicing
            min_gray: The minimum gray level to preserve
            max_gray: The maximum gray level to preserve
            preserve_original: Whether to preserve the original values of unselected areas

        Returns:
            The sliced image
        """
        assert 0 <= min_gray <= 255, "Min gray level must be between 0 and 255"
        image_array = np.array(image)

        # Create a mask for the selected gray levels
        mask = (image_array >= min_gray) & (image_array <= max_gray)

        # Create a new image with the selected gray levels
        new_image = np.zeros_like(image_array)

        # Slice the image using the mask
        new_image[mask] = 255

        # Preserve the original values of unselected areas
        if preserve_original:
            new_image[~mask] = image_array[~mask]

        return Image.fromarray(new_image)

    @staticmethod
    def histogram_equalization(image: Image.Image) -> Image.Image:
        """
        Perform histogram equalization on a grayscale image
        Args:
            image: The input image to apply histogram equalization
        Returns:
            The equalized image
        """
        return Image.fromarray(cv2.equalizeHist(np.array(image)))

    @staticmethod
    def bit_plane_image(image: Image.Image, bit_plane: int) -> Image.Image:
        """
        Display the bit-plane images for the input image
        Args:
            image: The input image to apply bit-plane image
            bit_plane: The bit-plane image to be displayed
        Returns:
            The bit-plane image
        """
        assert 0 <= bit_plane <= 7, "Bit-plane level must be between 0 and 7"

        # Extract the specified bit-plane by bitwise shifting and masking
        bit_plane_image = (np.array(image) >> bit_plane) & 1

        # Scale the bit-plane image to the full 0-255 range for display purposes
        bit_plane_image = bit_plane_image * 255

        return Image.fromarray(bit_plane_image)

    @staticmethod
    def smooth_image(image: Image.Image, smoothing_level: int) -> Image.Image:
        """
        Smooth the image
        Args:
            image: The input image to apply smoothing
            smoothing_level: The level of smoothing
        Returns:
            The smoothed image
        """
        assert smoothing_level > 0, "Smoothing level must be greater than 0"
        # As kernel size must be odd, we multiply the smoothing level by 2 and add 1
        smoothing_level = int(2 * smoothing_level + 1)

        # Apply Gaussian blur to the image
        return Image.fromarray(cv2.GaussianBlur(np.array(image), (smoothing_level, smoothing_level), 0))

    @staticmethod
    def sharpen_image(image: Image.Image, sharpening_level: int) -> Image.Image:
        """
        Sharpen the image
        Args:
            image: The input image to apply sharpening
            sharpening_level: The level of sharpening
        Returns:
            The sharpened image
        """
        image_array = np.array(image)

        # Create a Laplacian filter
        laplacian = cv2.Laplacian(image_array, cv2.CV_64F)
        sharpened_image = image_array - sharpening_level * laplacian

        # Clip the result
        sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

        return Image.fromarray(sharpened_image)

    @staticmethod
    def apply_average_mask(image: Image.Image, kernel_size: int) -> Image.Image:
        """
        Apply a 3x3 average filter to image using OpenCV
        Args:
            image: The input image to apply the average mask
            kernel_size: The size of the kernel for the average
        Returns:
            The image with the average mask applied
        """
        assert kernel_size % 2 == 1, "Kernel size must be odd"

        # Convert the main image to OpenCV format
        image_array = np.array(image)

        if USE_MANUALLY_FUNCTION:
            # The average mask is a kernel of ones divided by the kernel size squared
            mask = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

            # Call the convolution function to apply the mask
            filtered_array = ImageProcessorCore.convolution(image_array, mask)
        else:
            # Apply the average mask using OpenCV
            filtered_array = cv2.blur(image_array, (kernel_size, kernel_size))

        return Image.fromarray(filtered_array)

    @staticmethod
    def apply_median_mask(image: Image.Image, kernel_size: int) -> Image.Image:
        """
        Apply a median filter to image using OpenCV
        Args:
            image: The input image to apply the median mask
            kernel_size: The size of the kernel for the median
        Returns:
            The image with the median mask applied
        """
        assert kernel_size % 2 == 1, "Kernel size must be odd"

        # Convert the main image to OpenCV format
        image_array = np.array(image)

        if USE_MANUALLY_FUNCTION:
            filtered = np.zeros_like(image_array)
            padding = kernel_size // 2
            for i in range(padding, image_array.shape[0] - padding):
                for j in range(padding, image_array.shape[1] - padding):
                    region = image_array[i - padding:i + padding + 1, j - padding:j + padding + 1]
                    filtered[i, j] = np.median(region)
        else:
            # Apply the median mask using OpenCV
            filtered = cv2.medianBlur(image_array, kernel_size)

        return Image.fromarray(filtered)

    @staticmethod
    def apply_laplacian_mask(image: Image.Image) -> Image.Image:
        """
        Apply a Laplacian mask to the image using OpenCV
        Args:
            image: The input image to apply the Laplacian mask
        Returns:
            The image with the Laplacian mask applied
        """
        # Convert the main image to OpenCV format
        image_array = np.array(image)

        if USE_MANUALLY_FUNCTION:
            # The laplacian mask
            laplacian_mask = np.array([
                [0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]
            ])

            # Call the convolution function to apply the mask
            filtered_array = ImageProcessorCore.convolution(image_array, laplacian_mask)
        else:
            # Apply the Laplacian mask using OpenCV
            filtered_array = cv2.Laplacian(image_array, cv2.CV_64F)
            filtered_array = np.clip(filtered_array, 0, 255).astype(np.uint8)

        return Image.fromarray(filtered_array)
