salon = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def selection():
    row = int(input('Select the row number you want to reserve:  '))
    chair = int(input('Select the desired seat number for reservation : '))
    return row, chair


# row, chair = selection()
def check_capacity(row, chair):
    if salon[row][chair] == 0:
        return True
    else:
        return False


def reservation():
    row, chair = selection()
    status = check_capacity(row, chair)
    if status:
        reserved_place = salon[row][chair] == 1
        print(f'Seat {chair} in row {row} has been successfully reserved for you ')
    else:
        print('The requested position is filled. Please choose another option')
        reservation()


reservation()