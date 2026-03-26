import sys


def pError(error):
    print(f"AssertionError: {error}")
    exit()


def EvenOdd(nbr):
    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


lenght = len(sys.argv)
if lenght > 2:
    pError("more than one argument is provided")
elif lenght == 1:
    exit()

try:
    nbr = int(sys.argv[1])
    EvenOdd(nbr)
except ValueError:
    pError("argument is not an integer")
