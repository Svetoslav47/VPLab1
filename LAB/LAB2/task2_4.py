def main():
    n = int(input('n = '))
    while (n <= 0):
        n = int(input('n трябва да е положително число n = '))

    is_prime = n > 1
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f'{n} е просто число')
    else:
        print(f'{n} не е просто число')


if __name__ == '__main__':
    main()
