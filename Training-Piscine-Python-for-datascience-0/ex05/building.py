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


def my_counter(str):
    """
    Count the occurrences of different character types in a string.
    Args:
        str (str): Input string.
    Returns:
        none.
    """

    punct_set = set(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    print(f'The text contains {len(str)} characters: ')
    print(f'{sum(1 for c in str if c.isupper())} upper letters')
    print(f'{sum(1 for c in str if c.islower())} lower letters')
    print(f'{sum(1 for c in str if c in punct_set)} punctuation marks')
    print(f'{sum(1 for c in str if c.isspace())} spaces')
    print(f'{sum(1 for c in str if c.isdigit())} digits')


def main(argv):
    """
    Main function of the building program.

    Args:
        argv (list): List of command line arguments.

    Returns:
        None: This function does not return a value.
    """

    count = len(argv)
    if count == 0:
        try:
            print("What is the text to count?")
            text = sys.stdin.read()
        except ValueError:
            print("No text to count")
            exit()
        my_counter(text)
    elif count == 1:
        my_counter(argv[0])
    else:
        pError("more than one argument is provided")


if __name__ == "__main__":
    main(sys.argv[1:])
