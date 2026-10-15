def main():
    x = float(input('x = '))

    if 1 <= x <= 10:
        print(f'{x} се намира в интервала [1; 10]')
    else:
        print(f'{x} се намира извън интервала [1; 10]')


if __name__ == '__main__':
    main()
