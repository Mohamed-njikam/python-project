cells = '_________'
field = [[cells[0], cells[1], cells[2]],
         [cells[3], cells[4], cells[5]],
         [cells[6], cells[7], cells[8]]]

field2 = [cells[0], cells[1], cells[2],
         cells[3], cells[4], cells[5],
         cells[6], cells[7], cells[8]]

count_X = cells.count('X')
count_O = cells.count('O')

print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")

cell_filled = False


def fill_cell(coordinate, symbol):
    global cell_filled
    if int(coordinate[0]) == 1 and int(coordinate[1]) == 1:
        if field[2][0] == '_':
            cell_filled = True
            field[2][0] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 2 and int(coordinate[1]) == 1:
        if field[2][1] == '_':
            cell_filled = True
            field[2][1] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 3 and int(coordinate[1]) == 1:
        if field[2][2] == '_':
            cell_filled = True
            field[2][2] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 1 and int(coordinate[1]) == 2:
        if field[1][0] == '_':
            cell_filled = True
            field[1][0] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 2 and int(coordinate[1]) == 2:
        if field[1][1] == '_':
            cell_filled = True
            field[1][1] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 3 and int(coordinate[1]) == 2:
        if field[1][2] == '_':
            cell_filled = True
            field[1][2] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 1 and int(coordinate[1]) == 3:
        if field[0][0] == '_':
            cell_filled = True
            field[0][0] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 2 and int(coordinate[1]) == 3:
        if field[0][1] == '_':
            cell_filled = True
            field[0][1] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')
    elif int(coordinate[0]) == 3 and int(coordinate[1]) == 3:
        if field[0][2] == '_':
            cell_filled = True
            field[0][2] = symbol
            print(f"""---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------""")
        else:
            cell_filled = False
            print('This cell is occupied! Choose another one!')


def get_state():
    row_x1 = field[0][0] == field[0][1] == field[0][2] == 'X'  # 3 Xs in a row
    row_x2 = field[1][0] == field[1][1] == field[1][2] == 'X'
    row_x3 = field[2][0] == field[2][1] == field[2][2] == 'X'
    rows_x = row_x1 or row_x2 or row_x3
    rowsx = row_x1 and row_x2 and row_x3

    col_x1 = field[0][0] == field[1][0] == field[2][0] == 'X'
    col_x2 = field[0][1] == field[1][1] == field[2][1] == 'X'
    col_x3 = field[0][2] == field[1][2] == field[2][2] == 'X'
    cols_x = col_x1 or col_x2 or col_x3
    colsx = col_x1 and col_x2 and col_x3

    obl_x1 = field[0][0] == field[1][1] == field[2][2] == 'X'
    obl_x2 = field[0][2] == field[1][1] == field[2][0] == 'X'
    obls_x = obl_x1 or obl_x2
    oblsx = obl_x1 and obl_x2

    row_o1 = field[0][0] == field[0][1] == field[0][2] == 'O'  # 3 Xs in a row
    row_o2 = field[1][0] == field[1][1] == field[1][2] == 'O'
    row_o3 = field[2][0] == field[2][1] == field[2][2] == 'O'
    rows_o = row_o1 or row_o2 or row_o3
    rowso = row_o1 and row_o2 and row_o3

    col_o1 = field[0][0] == field[1][0] == field[2][0] == 'O'
    col_o2 = field[0][1] == field[1][1] == field[2][1] == 'O'
    col_o3 = field[0][2] == field[1][2] == field[2][2] == 'O'
    cols_o = col_o1 or col_o2 or col_o3
    colso = col_o1 and col_o2 and col_o3

    obl_o1 = field[0][0] == field[1][1] == field[2][2] == 'O'
    obl_o2 = field[0][2] == field[1][1] == field[2][0] == 'O'
    obls_o = obl_o1 or obl_o2
    oblso = obl_o1 and obl_o2

    if abs(count_X - count_O) not in (1, 0) or any([rows_x, cols_x, obls_x]) and any([rows_o, cols_o, obls_o]):
        return 'Impossible'

    elif any([rows_x, cols_x, obls_x]):
        return 'X wins'

    elif any([rows_o, cols_o, obls_o]):
        return 'O wins'

    elif all([not rowsx, not colsx, not oblsx, not rowso, not colso, not oblso, '_' not in field2]):
        return 'Draw'

    elif all([not rowsx, not colsx, not oblsx, not rowso, not colso, not oblso, '_' in field2]):
        return 'Game not finished'


counter = 1

while counter != 10:
    if counter % 2 == 0:
        symb = 'O'
    else:
        symb = 'X'
    while not cell_filled:
        coordinates = input('Enter the coordinates: ').split()
        try:
            if not coordinates[0].isnumeric() or not coordinates[1].isnumeric():
                print('You should enter numbers!')
            elif int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
            else:
                fill_cell(coordinates, symb)
        except IndexError as index_:
            print('You should enter numbers!')

    cell_filled = False
    if get_state() in ['X wins', 'O wins', 'Draw']:
        print(get_state())
        break
    elif counter == 9:
        print('Draw')
    counter += 1
