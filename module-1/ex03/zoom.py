from load_image import ft_load, display_with_axes
import numpy as np


def zoom_image(image, start_x=450, start_y=100, size=400):
    """
    Zoom into a portion of the image and convert to grayscale

    Parameters:
        image_array (numpy.ndarray): Original image array
        start_y (int): Starting Y coordinate for zoom
        start_x (int): Starting X coordinate for zoom
        size (int): Size of the zoom window

    Returns:
        numpy.ndarray: Zoomed portion of the image in grayscale
    """
    try:

        if image is None:
            return None
        zoomed = image[start_y:start_y+size, start_x:start_x+size]
        if len(zoomed.shape) == 3:
            zoomed = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

        print(
            f"New shape after slicing: {zoomed.shape}",
            zoomed,
            sep='\n'
        )
        return zoomed

    except Exception as e:
        print(f"Error during zoom operation: {str(e)}")
        return None


def main():
    image = ft_load("animal.jpeg")
    if image is not None:
        zoomed_image = zoom_image(image)
        if zoomed_image is not None:
            display_with_axes(zoomed_image)


if __name__ == "__main__":
    main()
