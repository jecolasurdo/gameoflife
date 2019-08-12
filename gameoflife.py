'''
    1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2. Any live cell with more than three live neighbours dies, as if by overcrowding.
    3. Any live cell with two or three live neighbours lives on to the next generation.
    4. Any dead cell with exactly three live neighbours becomes a live cell.
'''

import random


def main():
    m = generate_matrix()
    while True:
        draw_matrix(m)
        m = evolve_matrix(m)


def generate_matrix():
    '''
    creates a 20x20 matrix and randomly populates cells within the matrix.
    '''
    random.seed(a=1)
    matrix = []
    for r in range(20):
        row = []
        for c in range(20):
            row.append(random.randint(0, 1))
        matrix.append(row)

    return matrix


def evolve_matrix(matrix):
    for r in range(20):
        for c in range(20):
            neighbors = get_neighbor_addresses((r, c))
            active_neigbor_count = count_active_neighbors(
                neighbors, matrix)
            cell_value = matrix[r][c]
            matrix[r][c] = apply_rule_to_cell(cell_value, active_neigbor_count)
    return matrix


def get_neighbor_addresses(cell):
    '''
    Returns an array of tuples representing the coordinates of the cells that
    surround the supplied coordinate.

    (r-1, c-1), (r-1, c+0), (r-1, c+1)
    (r-0, c-1), ----------, (r-0, c+1)
    (r+1, c-1), (r+1, c+0), (r+1, c+1)
    '''
    r, c = cell[0], cell[1]

    return [(r-1, c-1),
            (r-1, c+0),
            (r-1, c+1),
            (r-0, c-1),
            (r-0, c+1),
            (r+1, c-1),
            (r+1, c+0),
            (r+1, c+1)]


def count_active_neighbors(neighbor_addresses, matrix):
    '''
    Takes an array of 8 two-tuple coordinates, and a matrix.
    Inspects the cells at each of the 8 addresses, and returns the count of
    cells that are live.
    '''
    live_neighbor_count = 0
    for address in neighbor_addresses:
        if address[0] < 0 or address[1] < 0 or address[0] > 19 or address[1] > 19:
            continue
        if matrix[address[0]][address[1]] == 1:
            live_neighbor_count += 1
    return live_neighbor_count


def apply_rule_to_cell(cell_value, active_neighbor_count):
    if active_neighbor_count == 3:
        return 1
    if active_neighbor_count not in [2, 3]:
        return 0


CELL_ACTIVE = " " + u'\u26aa' + " "
CELL_INACTIVE = "   "
BORDER_LEFT_RIGHT = u'\u2502'
CORNER_NW = u'\u250c'
CORNER_NE = u'\u2510'
CORNER_SW = u'\u2514'
CORNER_SE = u'\u2518'
BORDER_TOP_BOTTOM = u'\u2500'


def draw_matrix(matrix):
    '''
    prints the supplied matrix to the screen
    '''
    print(CORNER_NW.ljust(len(matrix)*len(CELL_ACTIVE) +
                          1, BORDER_TOP_BOTTOM) + CORNER_NE)
    for r in matrix:
        print(BORDER_LEFT_RIGHT, end="")
        for c in r:
            print(CELL_ACTIVE, end="") if c == 1 else print(
                CELL_INACTIVE, end="")
        print(BORDER_LEFT_RIGHT)
    print(CORNER_SW.ljust(len(matrix)*len(CELL_INACTIVE) +
                          1, BORDER_TOP_BOTTOM) + CORNER_SE)


if __name__ == '__main__':
    main()
