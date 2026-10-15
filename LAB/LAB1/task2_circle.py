import math


def main():
    r = float(input('r = '))

    area = math.pi * r ** 2
    perimeter = 2 * math.pi * r
    print(f'Area = {area:.3f}')
    print(f'Perimeter = {perimeter:.3f}')


if __name__ == '__main__':
    main()
