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
    for r in range(20):
        for c in range(20):
            print("row {} columns {} value {}".format(r, c, random.randint(0,1)))

    return None

def draw_matrix(matrix):
    '''
    prints the supplied matrix to the screen
    '''
    print("done")


if __name__ == '__main__':
    main()