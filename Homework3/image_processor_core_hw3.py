import cv2
import numpy as np
from PIL import Image

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
    def hsi_image(image: Image.Image, color: str) -> Image.Image:
        """
        Get its “Hue component image”, “Saturation component image”, and “Intensity component image” and
        display them as 8-bit gray-level images respectively.

        Args:
            image (Image.Image): The image to process
            color (str): The color to extract

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
        if color == 'hue':
            result_array[:, :] = hsi_image[:, :, 0]
        elif color == 'saturation':
            result_array[:, :] = hsi_image[:, :, 1]
        elif color == 'intensity':
            result_array[:, :] = hsi_image[:, :, 2]

        return Image.fromarray(result_array.astype(np.uint8))
