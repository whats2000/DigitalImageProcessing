from tkinter import messagebox
from typing import TYPE_CHECKING

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
        Get its “Red component image”, “Green component image”, and “Blue component image” and
        display them as 24-bit color images respectively.
        """
        assert color in ['red', 'green', 'blue'], f"Invalid color: {color}"
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        main_filtered_image = ImageProcessorCore3.rgb_image(self.app.image, color)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.rgb_image(self.app.compare_image, color)
        self.app.update_image([main_filtered_image, compare_filtered_image])


    def hsi_image(self, channel: str):
        """
        Get its “Hue component image”, “Saturation component image”, and “Intensity component image” and
        display them as 8-bit gray-level images respectively.
        """
        assert channel in ['hue', 'saturation', 'intensity'], f"Invalid channel: {channel}"
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        main_filtered_image = ImageProcessorCore3.hsi_image(self.app.image, channel)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.hsi_image(self.app.compare_image, channel)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def complement_image(self):
        """
        Get the complement of the image and compare image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        main_filtered_image = ImageProcessorCore3.complement_image(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.complement_image(self.app.compare_image)
        self.app.update_image([main_filtered_image, compare_filtered_image])


    def rgb_histogram_equalization(self):
        """
        Perform histogram equalization on the RGB image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "No image to process")
            return

        main_filtered_image = ImageProcessorCore3.histogram_equalization(self.app.image)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.histogram_equalization(self.app.compare_image)
        self.app.update_image([main_filtered_image, compare_filtered_image])