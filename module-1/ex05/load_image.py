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
    

def display(image, image1, image2, image3, image4, image5):
    """
    Display the zoomed images in a grid with axis scales.
    
    Parameters:
        image (numpy.ndarray): First image array to display.
        image1 (numpy.ndarray): Second image array to display.
        image2 (numpy.ndarray): Third image array to display.
        image3 (numpy.ndarray): Fourth image array to display.
        image4 (numpy.ndarray): Fifth image array to display.
        image5 (numpy.ndarray): Sixth image array to display.
    """
    plt.figure(figsize=(10, 10))

    plt.subplot(3, 2, 1)
    plt.imshow(image)
    plt.title("Figure VIII.1: Original")
    plt.axis('off')

    plt.subplot(3, 2, 2)
    plt.imshow(image1)
    plt.title("Figure VIII.2: Invert")
    plt.axis('off')

    plt.subplot(3, 2, 3)
    plt.imshow(image2)
    plt.title("Figure VIII.3: Red")
    plt.axis('off')

    plt.subplot(3, 2, 4)
    plt.imshow(image3)
    plt.title("Figure VIII.4: Green")
    plt.axis('off')

    plt.subplot(3, 2, 5)
    plt.imshow(image4)
    plt.title("Figure VIII.5: Blue")
    plt.axis('off')

    plt.subplot(3, 2, 6)
    plt.imshow(image5, cmap='gray')
    plt.title("Figure VIII.6: Grey")
    plt.axis('off')

    plt.show()
