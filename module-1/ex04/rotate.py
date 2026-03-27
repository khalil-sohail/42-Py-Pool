from load_image import ft_load, display_with_axes
import numpy as np
from PIL import Image

def manual_transpose(image_array):
    """
    Manually transpose the image (rotate by 90 degrees counterclockwise).
    
    Parameters:
        image_array (numpy.ndarray): Image array to transpose.
        
    Returns:
        numpy.ndarray: Transposed image array.
    """
    height, width = image_array.shape
    transposed = np.zeros((width, height), dtype=image_array.dtype)
    
    for i in range(height):
        for j in range(width):
            transposed[j, -1 * (height - i - 1)] = image_array[i, j]
    
    return transposed

def rotate_image(image, start_x=450, start_y=100, size=400):
    """
    Extract a portion of the image, convert to grayscale if necessary,
    and then rotate it by 90 degrees counterclockwise.
    
    Parameters:
        image (numpy.ndarray): Original image array.
        start_x (int): Starting X coordinate for zoom.
        start_y (int): Starting Y coordinate for zoom.
        size (int): Size of the zoom window.
        
    Returns:
        numpy.ndarray: Transposed (rotated) portion of the image in grayscale.
    """
    try:
        if image is None:
            print("Error: Image is None.")
            return None

        zoomed = image[start_y:start_y+size, start_x:start_x+size]

        if len(zoomed.shape) == 3:
            zoomed = np.mean(zoomed, axis=2).astype(np.uint8)

        zoomed = manual_transpose(zoomed)

        print(f"New shape after slicing and transposing: {zoomed.shape}")
        print(zoomed)
        return zoomed
        
    except Exception as e:
        print(f"Error during zoom operation: {str(e)}")
        return None

def main():
    image = ft_load("animal.jpeg")
    
    if image is not None:
        zoomed_image = rotate_image(image)
        if zoomed_image is not None:
            display_with_axes(zoomed_image)
        else:
            print("Error: Could not process the image.")
    else:
        print("Error: Image could not be loaded.")

if __name__ == "__main__":
    main()
