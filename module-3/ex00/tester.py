from S1E9 import Character, Stark


def main():
    Ned = Stark("Ned")
    print(f"Ned's dict: {Ned.__dict__}")
    print(f"Is Ned alive? {Ned.is_alive}")

    Ned.die()
    print(f"Is Ned alive after die()? {Ned.is_alive}")

    Lyanna = Stark("Lyanna", False)
    print(f"Lyanna's dict: {Lyanna.__dict__}")

    print(f"Stark class doc: {Stark.__doc__}")
    print(f"Stark __init__ doc: {Stark.__init__.__doc__}")
    print(f"Stark die() doc: {Stark.die.__doc__}")

    try:
        hodor = Character("hodor")
        print(
            "FAIL: Successfully instantiated Character! It must be abstract.",
            hodor
        )
    except TypeError as e:
        print(f"PASS: Prevented Character instantiation -> {e}")
    except Exception as e:
        print(
            "FAIL: Caught the wrong error! Expected TypeError,",
            f"got {type(e).__name__}",
            sep=" "
        )

    print(f"Is Stark a subclass of Character? {issubclass(Stark, Character)}")
    print(f"Is Ned an instance of Character? {isinstance(Ned, Character)}")


if __name__ == "__main__":
    main()
