import sys
import ft_filter


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
        # cmp = lambda x: True if len(x) > nbr else False
        filtered = ft_filter(lambda x: len(x) > nbr, my_list)
        list = [item for item in my_list if filtered(item)]
        print(list)
    except ValueError:
        pError("the arguments are bad.")


if __name__ == '__main__':
    main(sys.argv[1:])
