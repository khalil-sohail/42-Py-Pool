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
    if len(argv) != 1:
        pError("the arguments are bad.")

    try:
        NESTED_MORSE = {
            " ": '/',       'A': '.-',
            'B': '-...',    'C': '-.-.',
            'D': '-..',     'E': '.',
            'F': '..-.',    'G': '--.',
            'H': '....',    'I': '..',
            'J': '.---',    'K': '-.-',
            'L': '.-..',    'M': '--',
            'N': '-.',      'O': '---',
            'P': '.--.',    'Q': '--.-',
            'R': '.-.',     'S': '...',
            'T': '-',       'U': '..-',
            'V': '...-',    'W': '.--',
            'X': '-..-',    'Y': '-.--',
            'Z': '--..',    '1': '.----',
            '2': '..---',   '3': '...--',
            '4': '....-',   '5': '.....',
            '6': '-....',   '7': '--...',
            '8': '---..',   '9': '----.',
            '0': '-----',
        }
        s = str(argv[0])
        punctuation = set(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
        if not isinstance(s, str) or any(c in punctuation for c in s):
            raise ValueError("the arguments are bad.")
        for i, letter in enumerate(s):
            print(
                NESTED_MORSE[letter.upper()] +
                (' ' if i < len(s) - 1 else ''),
                end=''
            )
        print()
    except ValueError as e:
        pError(e)


if __name__ == '__main__':
    main(sys.argv[1:])
