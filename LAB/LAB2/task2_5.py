def main():
    day = int(input('Номер на ден (1-7): '))

    if day == 1:
        name = 'понеделник'
    elif day == 2:
        name = 'вторник'
    elif day == 3:
        name = 'сряда'
    elif day == 4:
        name = 'четвъртък'
    elif day == 5:
        name = 'петък'
    elif day == 6:
        name = 'събота'
    elif day == 7:
        name = 'неделя'
    else:
        name = None

    if name:
        print(f'Ден {day} е {name}')
    else:
        print(f'{day} не е валиден номер на ден')


if __name__ == '__main__':
    main()
