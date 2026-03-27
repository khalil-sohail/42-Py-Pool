import numpy as np


def pError(error):
    """
    print an error.
    Args:
        error (str): The error to print.
    Returns:
        none.
    """

    print(f"AssertionError: {error}")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    give_bmi(height: list[int | float], weight: list[int | float])
        -> list[int | float].
    Args:
        height (list):  list of integers or floats represents height.
        weight (list):  list of integers or floats represents weight.
    Returns:
        res (list): returns a list of BMI values.
    """

    if not isinstance(height, list) or not isinstance(weight, list):
        pError("Invalid argument.")
        return []
    if len(height) != len(weight):
        pError("Invalid argument.")
        return []
    valid_h = all(isinstance(i, (int, float))
                  and not isinstance(i, bool) for i in height)
    valid_w = all(isinstance(i, (int, float))
                  and not isinstance(i, bool) for i in weight)

    if not valid_h or not valid_w:
        pError("Invalid argument.")
        return []
    if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
        pError("Invalid argument.")
        return []

    Hitem = np.array(height) * np.array(39.37)
    Witem = np.array(weight) * np.array(2.205)

    res = (Witem * 703) / Hitem**2

    return res.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    Args:
        height (list):  list of integers or floats represents height.
        weight (list):  list of integers or floats represents weight.
    Returns:
        res (list): returns a list of BOOLEN values.
    """

    valid_bmi = all(isinstance(i, (int, float))
                    and not isinstance(i, bool) for i in bmi)

    if (not valid_bmi or not isinstance(limit, int) or limit <= 0):
        pError("Invalid argument")
        return ([])

    bmi_arr = np.array(bmi)
    bool_arr = bmi_arr > limit

    return bool_arr.tolist()
