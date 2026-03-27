import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, slices it based on start/end,
    prints the new shape, and returns the sliced 2D array.
    """
    if not isinstance(family, list):
        raise AssertionError("family must be a list.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("start and end indices must be integers.")

    if not family or not all(isinstance(row, list) for row in family):
        raise AssertionError("family must be a 2D list.")

    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise AssertionError("The 2D array must be rectangular.")

    for row in family:
        valid_types = all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in row
        )
        if not valid_types:
            raise AssertionError("All elements must be int or float.")

    arr = np.array(family)
    new_arr = arr[start:end]
    print(f'My shape is : {arr.shape}')
    print(f'My new shape is : {new_arr.shape}')
    return new_arr
