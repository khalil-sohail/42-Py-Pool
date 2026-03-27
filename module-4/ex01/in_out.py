def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return x**2

def pow(x: int | float) -> int | float:
    """Returns the exponentiation of x by itself (x^x)."""
    return x**x

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal x
        count = function(x)
        x = count
        return count
        
    return inner