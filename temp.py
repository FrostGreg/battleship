def main():
    board = ["1", "M", "1", " ", " ", "1", "M", "M",
             "1", "1", "1", " ", " ", "1", "3", "M",
             " ", " ", " ", " ", " ", " ", "1", "1",
             "1", "1", "1", " ", " ", " ", " ", " ",
             "1", "M", "1", "1", "1", "1", " ", " ",
             "1", "1", "1", "1", "M", "1", " ", " ",
             "1", "1", "2", "2", "2", "1", " ", " ",
             "1", "M", "2", "M", "1", " ", " ", " "]
    selected = []
    columns = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    row = ["A", "B", "C", "D", "E", "F", "G", "H"]

    print_board(board, selected, columns, row)

    while 1:
        board_mask(board, selected, columns, row)


def print_board(board, selected, columns, row):
    for i in range(len(columns)):
        print("  " + columns[i], end="  ")

    x = 0
    print("")
    for i in range(len(row)):
        print("  " + row[i], end="  ")
        for j in range(8):
            if x in selected:
                print("  " + board[x], end="  ")
            else:
                print("  *", end="  ")
            x += 1
        print("")


def board_mask(board, selected, columns, row):
    row_input = input("Enter Row: ")
    while row_input.upper() not in row:
        row_input = input("Enter Row: ")

    column_input = int(input("Enter Column: "))
    while column_input < 1 or column_input > 9:
        column_input = int(input("Enter Column: "))

    for i in range(len(row)):
        if row_input.upper() == row[i]:
            row_input = i + 1
            break
    n = (4 * row_input) - 9
    y = (4 * row_input) + column_input + n
    selected.append(y)
    print_board(board, selected, columns, row)


if __name__ == "__main__":
    main()
