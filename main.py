def display(array):
    for x in range(50):
        for y in range (50):
            if (y != 49):
                print("[",array[x][y],"]", end =" ", sep='')
            else:
                print("[",array[x][y],"]",sep='')


def main():
    xVal, yVal = 50, 50
    Matrix = [[(x+1) for x in range(xVal)] for y in range(yVal)]

    display(Matrix)

main()