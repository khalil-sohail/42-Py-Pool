import sys


def pError(error):
    """
    print an error.
    Args:
        error (str): The error to print.
    Returns:
        none.
    """

    print(f"AssertionError: {error}")
    exit()


def main(argv):
    if len(argv) != 2:
        pError("the arguments are bad.")

    try:
        my_list = str(argv[0]).split()
        nbr = int(argv[1])
        result = [item for item in my_list if (lambda x: len(x) > nbr)(item)]
        print(result)
    except ValueError:
        pError("the arguments are bad.")


if __name__ == '__main__':
    main(sys.argv[1:])
