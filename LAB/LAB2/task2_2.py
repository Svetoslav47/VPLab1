def main():
    n = int(input('n = '))
    while (n <= 0):
        n = int(input('n трябва да е положително число n = '))
        
    total = 0

    for i in range(n):
        num = int(input())
        total += num

    print(f'Сума = {total}')


if __name__ == '__main__':
    main()
