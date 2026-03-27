from array2D import slice_me


def main():
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]

        print("--- Valid Data (Subject Examples) ---")
        print(slice_me(family, 0, 2))
        print("\n---")
        print(slice_me(family, 1, -2))

        print("\n--- Advanced Slicing Edge Cases ---")

        print("\n1. Overshooting the End Index:")
        print(slice_me(family, 0, 100))

        print("\n2. Start Index Greater Than End Index:")
        # In standard Python, this results in an empty list []
        print(slice_me(family, 3, 1))

        print("\n3. Extreme Negative Indices:")
        # Should slice from the back
        print(slice_me(family, -4, -1))

        print("\n--- Error Handling (Defense Preparation) ---")

        print("\n4. Argument is not a list:")
        print(slice_me("I am a string, not a matrix", 0, 2))  # type: ignore

        print("\n5. Indices are not integers:")
        print(slice_me(family, 0.5, 2.5))  # type: ignore

        print("\n6. Not a true 2D Array (Inconsistent row sizes):")
        bad_matrix = [[1.80, 78.4],
                      [2.15],
                      [2.10, 98.5, 10.0]]
        print(slice_me(bad_matrix, 0, 2))

    except AssertionError as e:
        print(f"Caught an assertion error: {e}")
    except Exception as e:
        print(f"Caught an unexpected error: {e}")


if __name__ == "__main__":
    main()
