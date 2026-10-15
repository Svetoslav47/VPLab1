def main():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    pay = hours * rate
    print(f'Pay: {pay:.2f}')


if __name__ == '__main__':
    main()
