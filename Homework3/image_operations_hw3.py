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

    def apply_averaging_mask(self, mask_size: int = 3):
        """
        Apply an averaging mask to both the main and comparison images using OpenCV.

        Args:
            mask_size (int): The size of the averaging mask
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore3.apply_average_mask(self.app.image, mask_size)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.apply_average_mask(self.app.compare_image, mask_size)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def apply_sharpening_mask(self, model: str):
        """
        Apply a sharpening mask to both the main and comparison images using OpenCV.
        """
        assert model in ['rgb', 'hsi'], f"Invalid model: {model}"

        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore3.apply_sharpening_mask(self.app.image, model)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.apply_sharpening_mask(self.app.compare_image, model)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def hue_mask(self, lower_hue: int, upper_hue: int):
        """
        Apply a hue mask to the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore3.hue_mask(self.app.image, lower_hue, upper_hue)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.hue_mask(self.app.compare_image, lower_hue, upper_hue)
        self.app.update_image([main_filtered_image, compare_filtered_image])

    def saturation_mask(self, lower_saturation: int, upper_saturation: int):
        """
        Apply a saturation mask to the image
        """
        if not self.app.image:
            messagebox.showinfo("Info", "Please open an image first")
            return

        main_filtered_image = ImageProcessorCore3.saturation_mask(self.app.image, lower_saturation, upper_saturation)

        if not self.app.compare_image:
            self.app.update_image([main_filtered_image, None])
            return

        compare_filtered_image = ImageProcessorCore3.saturation_mask(self.app.compare_image, lower_saturation,
                                                                     upper_saturation)
        self.app.update_image([main_filtered_image, compare_filtered_image])
