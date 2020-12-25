grid = []
open_set = []
path = []
P = []
for s in range(100):
    P.append([-1])


class child:
    def __init__(self, parent, row, col, g, h, f):
        self.parent = parent
        self.row = row
        self.col = col
        self.g = g
        self.h = h
        self.f = f


# creating a board
def create_board():
    c = 10
    for i in range(9):
        grid.append([])
        for j in range(10):
            grid[i].append(str(c))
            c += 1


def display_board():
    for i in range(9):
        for j in range(10):
            print(grid[i][j], " ", end="")
        print()


def get_row_col(st, en):
    st_row = (st // 10) - 1
    st_col = st - (10 + st_row * 10)

    en_row = (en // 10) - 1
    en_col = en - (10 + en_row * 10)
    return st_row, st_col, en_row, en_col


create_board()
display_board()
start = int(input("Enter the start node number: "))
end = int(input("Enter the end node number: "))
start_row, start_col, end_row, end_col = get_row_col(start, end)
walls = []
no_of_wall = int(input("Enter the number of walls: "))
for i in range(no_of_wall):
    wall_no = int(input("Enter wall number: "))
    walls.append(wall_no)


def finding(parent, c_row, c_col):
    global open_set
    if 0 <= c_row <= 8 and 0 <= c_col <= 9:
        no = 10 + (c_row * 10) + c_col
        if parent not in P[no] and no not in walls:
            g = abs(start_row - c_row) + abs(start_col - c_col)
            h = abs(end_row - c_row) + abs(end_col - c_col)
            f = g + h
            ch1 = child(parent, c_row, c_col, g, h, f)
            open_set.append(ch1)
            P[parent].append(no)


def get_neighbors(start_node, st_row, st_col):
    finding(start_node, st_row - 1, st_col)
    finding(start_node, st_row, st_col + 1)
    finding(start_node, st_row + 1, st_col)
    finding(start_node, st_row, st_col - 1)


get_neighbors(start, start_row, start_col)


def get_min_f():
    print(open_set, [i.parent for i in open_set])
    mini = open_set[0].f
    min_no = open_set[0]
    for i in range(1, len(open_set)):
        if open_set[i].f < mini:
            mini = open_set[i].f
            min_no = open_set[i]
    return min_no


terminate = False
while not terminate:
    for i in open_set:
        if (10 + (i.row * 10) + i.col) == end:
            terminate = True
            break
    mi = get_min_f()
    par = 10 + (mi.row * 10) + mi.col
    open_set.clear()
    get_neighbors(par, mi.row, mi.col)
    path.append(mi)

for p in path:
    print(p.parent, " ", end="")
