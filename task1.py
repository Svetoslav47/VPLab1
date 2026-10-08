DIGITS = "0123456789ABCDEF"


def to_base(number, base):
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    number = abs(number)

    result = ""
    while number > 0:
        result = DIGITS[number % base] + result
        number //= base

    return sign + result


def read_integer():
    while True:
        text = input("Въведете цяло число: ").strip()
        try:
            return int(text)
        except ValueError:
            print(f"'{text}' не е валидно цяло число. Опитайте отново.")


def main():
    number = read_integer()

    print(f"Десетична:      {number}")
    print(f"Двоична:        {to_base(number, 2)}")
    print(f"Осмична:        {to_base(number, 8)}")
    print(f"Шестнайсетична: {to_base(number, 16)}")


if __name__ == "__main__":
    main()
