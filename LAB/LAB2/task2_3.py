def main():
    n = int(input('n = '))
    while (n <= 0):
        n = int(input('n трябва да е положително число n = '))

    for i in range(1, n + 1):
        print('*' * i)


if __name__ == '__main__':
    main()
