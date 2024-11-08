from tkinter import messagebox
from typing import TYPE_CHECKING

import numpy as np
from PIL import Image

from image_operations_hw2 import ImageOperationsHW2
from image_processor_core_hw3 import ImageProcessorCore3

if TYPE_CHECKING:
    from app import ImageProcessorApp


class ImageOperationsHW3(ImageOperationsHW2):
    def __init__(self, app: 'ImageProcessorApp'):
        super().__init__(app)
        self.app = app

    def rgb_image(self, color: str):
        """
        Get its “Red component image”, “Green component" image”, and “Blue component image” and
        display them as 24-bit color images respectively.
        """
        assert color in ['red', 'green', 'blue'], f"Invalid color: {color}"
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        # Update the compare image
        self.app.compare_image = ImageProcessorCore3.rgb_image(self.app.image, color)
        self.app.update_image([self.app.image, self.app.compare_image])


    def hsi_image(self, color: str):
        """
        Get its “Hue component image”, “Saturation component image”, and “Intensity component image” and
        display them as 24-bit color images respectively.
        """
        assert color in ['hue', 'saturation', 'intensity'], f"Invalid color: {color}"
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        # Update the compare image
        self.app.compare_image = ImageProcessorCore3.hsi_image(self.app.image, color)
        self.app.update_image([self.app.image, self.app.compare_image])
