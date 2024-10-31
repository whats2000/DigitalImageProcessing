import cv2
import numpy as np
from PIL import Image

# This is for working with the PIL library older
if not hasattr(Image, 'Resampling'):
    Image.Resampling = Image

USE_MANUALLY_FUNCTION = False


class ImageProcessorCore2:
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
            filtered_array = ImageProcessorCore2.convolution(image_array, mask)
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
            filtered_array = ImageProcessorCore2.convolution(image_array, laplacian_mask)
        else:
            # Apply the Laplacian mask using OpenCV
            filtered_array = cv2.Laplacian(image_array, cv2.CV_64F)
            filtered_array = np.clip(filtered_array, 0, 255).astype(np.uint8)

        return Image.fromarray(filtered_array)

    @staticmethod
    def apply_fft(image: Image.Image) -> Image.Image:
        """
        Apply Fast Fourier Transform to the image
        Args:
            image: The input image to apply FFT
        Returns:
            The image with FFT applied
        """
        # Convert the main image to OpenCV format
        image_array = np.array(image)

        # Apply FFT using numpy
        fft_result  = np.fft.fft2(image_array)
        fft_shifted  = np.fft.fftshift(fft_result)

        # Get the magnitude spectrum
        magnitude_spectrum = np.log(np.abs(fft_shifted) + 1)

        # Scale the magnitude spectrum to 0-255 for display
        scaled_magnitude = (magnitude_spectrum / np.max(magnitude_spectrum) * 255).astype(np.uint8)

        return Image.fromarray(scaled_magnitude)

    @staticmethod
    def inverse_fft_magnitude_only(image: Image.Image) -> Image.Image:
        """
        Perform inverse FFT using only the magnitude information of an image.
        Args:
            image (Image.Image): The input image.
        Returns:
            Image.Image: The reconstructed image from magnitude only.
        """
        # Convert the main image to OpenCV format
        image_array = np.array(image)

        # Apply FFT using numpy
        fft_result = np.fft.fft2(image_array)
        fft_shifted = np.fft.fftshift(fft_result)

        # Use only magnitude and set phase to zero
        magnitude = np.abs(fft_shifted)
        complex_spectrum = magnitude * np.exp(1j * 0)

        # Perform inverse FFT
        reconstructed_image = np.abs(np.fft.ifft2(np.fft.ifftshift(complex_spectrum)))

        # Clip the image to 0-255
        clipped_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)

        return Image.fromarray(clipped_image)

    @staticmethod
    def inverse_fft_phase_only(image: Image.Image) -> Image.Image:
        """
        Perform inverse FFT using only the phase information of an image.
        Args:
            image (Image.Image): The input image.
        Returns:
            Image.Image: The reconstructed image from phase only.
        """
        # Convert the main image to OpenCV format
        image_array = np.array(image)

        # Apply FFT using numpy
        fft_result = np.fft.fft2(image_array)
        fft_shifted = np.fft.fftshift(fft_result)

        # Use only phase and set magnitude to one
        phase = np.angle(fft_shifted)
        complex_spectrum = np.exp(1j * phase)

        # Perform inverse FFT
        reconstructed_image = np.abs(np.fft.ifft2(np.fft.ifftshift(complex_spectrum)))

        # Clip the image to 0-255 for display
        scaled_image = (reconstructed_image / np.max(reconstructed_image) * 255).astype(np.uint8)

        return Image.fromarray(scaled_image)

    @staticmethod
    def multiply_by_neg_1(image_array: np.array) -> np.array:
        """
        Multiply the image by (-1)^(x+y)
        Args:
            image_array: The input image to multiply
        Returns:
            The image multiplied by (-1)^(x+y)
        """
        x, y = np.indices(image_array.shape)
        result_array = image_array * ((-1) ** (x + y))
        return result_array

    @staticmethod
    def compute_dft(image_array: np.array) -> np.array:
        """
        Compute the DFT and return the magnitude spectrum.
        Args:
            image_array: The input image
        Returns:
            The magnitude spectrum of the DFT
        """
        return np.fft.fft2(image_array)

    @staticmethod
    def take_conjugate(fft_result: np.array) -> np.array:
        """
        Take the complex conjugate of the FFT result.
        Args:
            fft_result: The FFT result to conjugate
        Returns:
            The complex conjugate of the FFT result
        """
        return np.conj(fft_result)

    @staticmethod
    def compute_inverse_dft(fft_result: np.array) -> np.array:
        """
        Compute the inverse DFT and return the real part.
        Args:
            fft_result: The FFT result to transform
        Returns:
            The real part of the inverse DFT
        """
        return np.fft.ifft2(fft_result)
