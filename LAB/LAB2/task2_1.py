def main():
    n = int(input('n = '))
    max_num = int(input())

    for i in range(n - 1):
        num = int(input())
        if num > max_num:
            max_num = num

    print(f'Най-голямото число е {max_num}')


if __name__ == '__main__':
    main()
