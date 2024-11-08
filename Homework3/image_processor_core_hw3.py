import cv2
import numpy as np
from PIL import Image

from image_processor_core_hw2 import ImageProcessorCore2

# This is for working with the PIL library older
if not hasattr(Image, 'Resampling'):
    Image.Resampling = Image

USE_MANUALLY_FUNCTION = False


class ImageProcessorCore3:
    @staticmethod
    def rgb_image(image: Image.Image, color: str) -> Image.Image:
        """
        Get its “Red component image”, “Green component image”, and “Blue component image” and
        display them as 24-bit color images respectively.

        Args:
            image (Image.Image): The image to process
            color (str): The color to extract

        Returns:
            Image.Image: The processed image
        """
        image_array = np.array(image)
        result_array = np.zeros_like(image_array)

        # Apply the RGB model selection
        if color == 'red':
            result_array[:, :, 0] = image_array[:, :, 0]
        elif color == 'green':
            result_array[:, :, 1] = image_array[:, :, 1]
        elif color == 'blue':
            result_array[:, :, 2] = image_array[:, :, 2]

        return Image.fromarray(result_array.astype(np.uint8))

    @staticmethod
    def hsi_image(image: Image.Image, channel: str) -> Image.Image:
        """
        Get its “Hue component image”, “Saturation component image”, and “Intensity component image” and
        display them as 8-bit gray-level images respectively.

        Args:
            image (Image.Image): The image to process
            channel (str): The channel to extract

        Returns:
            Image.Image: The processed image
        """
        # Convert the image to HSI
        image_array = np.array(image)
        hsi_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)

        # For the result, we consider the image as 3D or 2D and select the channel
        result_array = np.zeros_like(image_array) \
            if image_array.ndim == 1 \
            else np.zeros((image_array.shape[0], image_array.shape[1]))

        # Apply the HSI model selection
        if channel == 'hue':
            result_array[:, :] = hsi_image[:, :, 0]
        elif channel == 'saturation':
            result_array[:, :] = hsi_image[:, :, 1]
        elif channel == 'intensity':
            result_array[:, :] = hsi_image[:, :, 2]

        return Image.fromarray(result_array.astype(np.uint8))

    @staticmethod
    def complement_image(image: Image.Image) -> Image.Image:
        """
        Get the complement of the image

        Args:
            image (Image.Image): The image to process

        Returns:
            Image.Image: The processed image
        """
        image_array = np.array(image)
        result_array = 255 - image_array

        return Image.fromarray(result_array.astype(np.uint8))


    @staticmethod
    def histogram_equalization(image: Image.Image) -> Image.Image:
        """
        Perform histogram equalization on the RGB image

        Args:
            image (Image.Image): The image to process

        Returns:
            Image.Image: The processed image
        """
        image_array = np.array(image)
        result_array = np.zeros_like(image_array)

        # Check image channels
        if image_array.ndim == 2:
            # Apply histogram equalization if the image is grayscale
            return Image.fromarray(cv2.equalizeHist(np.array(image)))
        else:
            # Apply histogram equalization for each channel
            for i in range(3):
                result_array[:, :, i] = cv2.equalizeHist(image_array[:, :, i])

        return Image.fromarray(result_array.astype(np.uint8))

    @staticmethod
    def apply_average_mask(image: Image.Image, kernel_size: int) -> Image.Image:
        """
        Apply a average filter to image using OpenCV
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
            filtered_array = ImageProcessorCore2.convolution(image_array, mask)
        else:
            # Apply the average mask using OpenCV
            filtered_array = cv2.blur(image_array, (kernel_size, kernel_size))

        return Image.fromarray(filtered_array)

    @staticmethod
    def apply_sharpening_mask(image: Image.Image, model: str) -> Image.Image:
        """
        Apply a sharpening mask to the image using OpenCV
        Args:
            image: The input image to apply the sharpening mask
            model: The model to use for sharpening
        Returns:
            The image with the sharpening mask applied
        """
        image_array = np.array(image)

        if model == 'rgb':
            # Create a Laplacian filter
            laplacian = cv2.Laplacian(image_array, cv2.CV_64F)
            sharpened_image = image_array - laplacian
            sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)
        elif model == 'hsi':
            # Convert the image to HSI
            hsi_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)

            # Split H, S, and V channels
            h, s, v = cv2.split(hsi_image)

            # Apply the Laplacian filter to the intensity channel
            laplacian = cv2.Laplacian(v, cv2.CV_64F)
            sharpened_image = v - laplacian
            sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

            # Merge the HSI channels
            sharpened_image = cv2.merge((h, s, sharpened_image))

            # Convert the image back to RGB
            sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_HSV2RGB)
        else:
            raise ValueError("Invalid sharpening model")

        return Image.fromarray(sharpened_image)