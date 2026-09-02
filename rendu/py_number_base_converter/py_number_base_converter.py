def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if from_base < 2 or from_base > 36:
        return "ERROR"

    if to_base < 2 or to_base > 36:
        return "ERROR"

    try:
        decimal_number = int(number, from_base)

    except ValueError:
        return "ERROR"

    result = ""

    while decimal_number > 0:

        remainder = decimal_number % to_base

        print(result)
        result = digits[remainder] + result
        print(result)

        decimal_number = decimal_number // to_base

    if result == "":
        return "0"

    return result


if __name__ == "__main__":
    print()
