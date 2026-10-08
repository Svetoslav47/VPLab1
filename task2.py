DIGITS = "0123456789ABCDEF"

BASES = {
    "2": (2, "двоично"),
    "8": (8, "осмично"),
    "16": (16, "шестнайсетично"),
}


def to_decimal(text, base):
    sign = -1 if text.startswith("-") else 1
    text = text.lstrip("-")

    result = 0
    for digit in text:
        result = result * base + DIGITS.index(digit)

    return sign * result


def is_valid(text, base):
    digits = text[1:] if text.startswith("-") else text
    return len(digits) > 0 and all(digit in DIGITS[:base] for digit in digits)


def read_base():
    while True:
        text = input("Изберете бройна система (2, 8 или 16): ").strip()
        if text in BASES:
            return BASES[text]
        print(f"'{text}' не е валиден избор. Опитайте отново.")


def read_number(base, name):
    while True:
        text = input(f"Въведете {name} число: ").strip().upper()
        if is_valid(text, base):
            return text
        print(f"'{text}' не е валидно {name} число. Опитайте отново.")


def main():
    base, name = read_base()
    number = read_number(base, name)

    print(f"Въведено ({base}): {number}")
    print(f"Десетична:   {to_decimal(number, base)}")


if __name__ == "__main__":
    main()
