"""
Construct a simple image processing tool with a graphic user interface (GUI),
providing the following functionalities:
1. Open/save/display 256-gray-level images in the format of JPG/TIF.
2. Adjust the contrast/brightness of images by changing the values of “a”
and “b” in 3 different methods:
(A) linearly (Y = aX +b);
(B) exponentially (Y = exp(aX+b));
(C) logarithmically (Y = ln(aX+b), b > 1).
3. Zoom in and shrink with respect to the images' original size by using
bilinear interpolation.
4. Rotate images by user-defined degrees.
5. Gray-level slicing: display images from a certain range of gray levels given
by users. 
Requirements: 
(1) users can define the range of gray levels to
be displayed; 
(2) users can choose either preserve the original values of unselected areas or 
display them as black color.
6. Display the histogram of images. An “auto-level” function by using histogram 
equalization should be provided.
7. Bit-Plane images: display the bit-plane images for the input image.
Requirements: users should be able to select which bit-plane image to be
displayed.
8. Smoothing and sharpening: providing smoothing and sharpening options
for the input images by using spatial filters. Requirements: the levels of
smoothing and sharpening should be defined by users via GUI.
"""
# First step is import the required libraries
import tkinter as tk


class ImageProcessorApp:
    def __init__(self, root_window: tk.Tk):
        """
        Initialize the ImageProcessorApp
        Args:
            root_window: The root window of the application
        """
        self.root = root_window
        self.root.title('Image Processor Tool')
        self.root.geometry('500x500')


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
