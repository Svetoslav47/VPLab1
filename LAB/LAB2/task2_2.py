def main():
    n = int(input('n = '))
    total = 0

    for i in range(n):
        num = int(input())
        total += num

    print(f'Сума = {total}')


if __name__ == '__main__':
    main()
