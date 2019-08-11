'''
    1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2. Any live cell with more than three live neighbours dies, as if by overcrowding.
    3. Any live cell with two or three live neighbours lives on to the next generation.
    4. Any dead cell with exactly three live neighbours becomes a live cell.
'''
import random

def main():
    m = generate_matrix()
    draw_matrix(m)

def generate_matrix():
    '''
    creates a 20x20 matrix and randomly populates cells within the matrix.
    '''
    random.seed(a=1)
    matrix = []
    for r in range(20):
        row = []
        for c in range(20):
            row.append(random.randint(0,1))
        matrix.append(row)

    return matrix

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
    print(CORNER_NW.ljust(len(matrix)*len(CELL_ACTIVE)+1, BORDER_TOP_BOTTOM) + CORNER_NE)
    for r in matrix:
        print(BORDER_LEFT_RIGHT, end="")
        for c in r:
            print(CELL_ACTIVE, end="") if c == 1 else print(CELL_INACTIVE, end="")
        print(BORDER_LEFT_RIGHT)
    print(CORNER_SW.ljust(len(matrix)*len(CELL_INACTIVE)+1, BORDER_TOP_BOTTOM) + CORNER_SE)

if __name__ == '__main__':
    main()