from give_bmi import give_bmi, apply_limit


def main():
    print("--- Valid Data (Subject Example) ---")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    print("\n--- Error Handling (Defense Preparation) ---")

    print("Different Sized Lists:")
    bad_size_bmi = give_bmi([1.75, 1.80], [70.0])
    print(f"Output: {bad_size_bmi}")

    print("\nInvalid Types in List:")
    bad_type_bmi = give_bmi([1.75, 1.80], [70.0, "eighty"])  # type: ignore
    print(f"Output: {bad_type_bmi}")

    print("\nZero Height (Division by Zero):")
    zero_height_bmi = give_bmi([1.75, 0.0], [70.0, 80.0])
    print(f"Output: {zero_height_bmi}")

    print("\napply_limit Error Handling:")
    bad_limit = apply_limit([22.5, 29.0], "twenty")  # type: ignore
    print(f"Bad Limit Output: {bad_limit}")

    bad_bmi_list = apply_limit([22.5, "error"], 26)  # type: ignore
    print(f"Bad BMI List Output: {bad_bmi_list}")

    print("\nArguments are not lists:")
    not_a_list = give_bmi(1.75, 70.0)  # type: ignore
    print(f"Output: {not_a_list}")

    print("\nEmpty Lists:")
    empty_bmi = give_bmi([], [])
    print(f"Output: {empty_bmi}")


if __name__ == "__main__":
    main()
