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

def draw_matrix(matrix):
    '''
    prints the supplied matrix to the screen
    '''
    print(u'\u250c'.ljust(len(matrix)*3+1,u'\u2500') + u'\u2510')
    for r in matrix:
        print(u'\u2502', end="")
        for c in r:
            print(" " + u'\u26aa' + " ", end="") if c == 1 else print("   ", end="")
        print(u'\u2502')
    print(u'\u2514'.ljust(len(matrix)*3+1,u'\u2500') + u'\u2518')

if __name__ == '__main__':
    main()