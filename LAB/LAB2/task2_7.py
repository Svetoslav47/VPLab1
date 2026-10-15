def main():
    a = float(input('Първо число: '))
    b = float(input('Второ число: '))
    op = input('Действие (+, -, *, /): ')

    if op == '+':
        print(f'Резултат: {a + b}')
    elif op == '-':
        print(f'Резултат: {a - b}')
    elif op == '*':
        print(f'Резултат: {a * b}')
    elif op == '/':
        if b == 0:
            print('Деление на нула не е възможно')
        else:
            print(f'Резултат: {a / b}')
    else:
        print('Невалидно действие')


if __name__ == '__main__':
    main()
