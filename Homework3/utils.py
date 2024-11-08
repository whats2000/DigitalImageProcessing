from tkinter import filedialog, messagebox, simpledialog
from typing import TYPE_CHECKING

import numpy as np
from PIL import Image

if TYPE_CHECKING:
    from app import ImageProcessorApp


def open_image(app: 'ImageProcessorApp', is_compare_image=False):
    """
    Open an image from the file dialog
    """
    file_path = filedialog.askopenfilename()

    # Prevent illegal file path
    if file_path == '':
        return

    # Try to open the image end .raw file as grayscale
    try:
        if file_path.lower().endswith('.raw'):
            # Ask the user for the image dimensions
            image_format = simpledialog.askstring("Input", "Enter the image format (e.g. 'L', 'RGB', 'RGBA'):")
            with open(file_path, "rb") as f:
                raw_data = f.read()

            # Check if the data size matches the expected dimensions, otherwise ask the user for the dimensions
            if len(raw_data) == 512 * 512:
                width = height = 512
            else:
                width = simpledialog.askinteger("Input", "Enter the image width:", minvalue=1)
                height = simpledialog.askinteger("Input", "Enter the image height:", minvalue=1)

            if not width or not height:
                print("Invalid dimensions provided.")
                return

            # Verify that the data size matches the expected dimensions
            expected_size = width * height
            if len(raw_data) != expected_size:
                print(
                    f"Warning: Data size ({len(raw_data)}) does not match expected size ({expected_size}) for {width}x{height} image.")

            # Load the image from the binary data
            image = Image.frombytes(image_format, (width, height), raw_data)
        else:
            image = Image.open(file_path)

        if is_compare_image and app.image is not None:
            app.compare_image = image
        else:
            app.image = image
            app.temp_array = np.array(image)

        app.update_image([app.image, app.compare_image])
    except Exception as e:
        messagebox.showinfo("Error", f"Error opening image: {e}")

def save_image(app: 'ImageProcessorApp', is_compare_image=False):
    """
    Save the image to a file
    """
    target_image = app.compare_image if is_compare_image else app.image

    if not target_image:
        messagebox.showinfo("Info", "Please open an image first")
        return

    file_name = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
    )

    if not file_name:
        return

    image_to_save = target_image.convert("RGB")
    image_to_save.save(file_name)

def remove_compare_image(app: 'ImageProcessorApp'):
    """
    Remove the compare image
    """
    app.compare_image = None
    app.update_image([app.image, None])
