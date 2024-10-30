from tkinter import filedialog, messagebox
from typing import TYPE_CHECKING

from PIL import Image

if TYPE_CHECKING:
    from app import ImageProcessorApp


def open_image(app: 'ImageProcessorApp'):
    """
    Open an image from the file dialog
    """
    file_path = filedialog.askopenfilename()

    # Prevent illegal file path
    if file_path == '':
        return

    # Update the image label with the new image
    app.update_image(Image.open(file_path))

def save_image(app: 'ImageProcessorApp'):
    """
    Save the image to a file
    """
    if not app.image:
        messagebox.showinfo("Info", "Please open an image first")
        return

    file_name = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
    )

    if not file_name:
        return

    image_to_save = app.image.convert("RGB")
    image_to_save.save(file_name)
