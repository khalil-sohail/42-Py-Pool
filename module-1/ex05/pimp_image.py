import numpy as np

def ft_invert(array) -> np.array:
    """invert: Inverts the color of the image received."""
    return 255 - array


def ft_red(array) -> np.array:
    """Red: Shows only the red component of the image."""
    res = array.copy()
    res[:, :, 1] = 0
    res[:, :, 2] = 0
    return res

def ft_green(array) -> np.array:
    """Green: Shows only the green component."""
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 2] = 0
    return res


def ft_blue(array) -> np.array:
    """Blue: Shows only the blue component."""
    res = array.copy()
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    return res


def ft_grey(array) -> np.array:
    """Grey: Converts the image to shades of gray."""
    grayscale = np.mean(array, axis=2, keepdims=True).astype(np.uint8)
    return grayscale
