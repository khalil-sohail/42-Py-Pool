import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.array:
    """
    Load an image and return its pixel content as a numpy array.
    The function prints the image format before returning the array.
    
    Parameters:
        path (str): The path to the image file
        
    Returns:
        numpy.array: Array containing the RGB pixel values
        
    return:
        returns None in case if error
    """

    try:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        arr = np.array(img)
        print(f'The shape of image is: {arr.shape}')
        print(arr)
        return arr

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None
    except IOError:
        print(f"Error: The file '{path}' is not a valid image or an unsupported format.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
        return None
    

def display_with_axes(zoomed_image):
    """
    Display the zoomed image with axis scales.
    
    Parameters:
        zoomed_image (numpy.ndarray): Image array to display.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(zoomed_image, cmap='gray')
    plt.title("Zoomed Image")
    plt.xlabel("X-axis (pixels)")
    plt.ylabel("Y-axis (pixels)")
    plt.show()
