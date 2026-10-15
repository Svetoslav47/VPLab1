def main():
    low = float(input('Долна граница: '))
    high = float(input('Горна граница: '))

    count = 0
    for i in range(10):
        num = float(input(f'Число {i + 1}: '))
        if low <= num <= high:
            count += 1

    print(f'Брой числа в интервала [{low}; {high}]: {count}')


if __name__ == '__main__':
    main()
