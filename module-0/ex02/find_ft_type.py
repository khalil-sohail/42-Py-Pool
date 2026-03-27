def all_thing_is_obj(object: any) -> int:
    t = type(object)

    if t.__name__ == "str":
        print(f'{object} is in the kitchen : {t}')
    else:
        print(f'{t.__name__} : {t}')
    return 42
