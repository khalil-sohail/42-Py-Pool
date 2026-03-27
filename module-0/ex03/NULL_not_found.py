def NULL_not_found(object: any) -> int:
    Nothing = None
    Zero = 0
    Empty = ''
    Fake = False

    if object is Nothing:
        print("Nothing: ", end="")
    elif object != object:
        print("Cheese: ", end="")
    elif isinstance(object, int) and object == Zero:
        print("Zero: ", end="")
    elif object is Empty:
        print("Empty:", end="")
    elif isinstance(object, bool) and object == Fake:
        print("Fake: ", end="")
    else:
        print('Type not Found')
        return 1

    print(f'{object} {type(object)}')
    return 0
