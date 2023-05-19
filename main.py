from enum import Enum

# class syntax
class TileState (Enum):
    empty = 0
    block = 1
    spawn = 2
    target = 3

def display(array):
    for x in range(50):
        for y in range (50):
            if (y != 49):
                print("[",array[x][y],"]", end =" ", sep='')
            else:
                print("[",array[x][y],"]",sep='')


def main():
    xVal, yVal = 50, 50
    Matrix = [[(TileState.empty.value) for x in range(xVal)] for y in range(yVal)]

    display(Matrix)



    spawnInput = str(input("input SPAWN location in the format of x,y"))
    spawnLocation = [spawnInput[0],spawnInput[2]]

    Matrix[int(spawnLocation[0])][int(spawnLocation[1])] = 2

    targetInput = str(input("input TARGET location in the format of x,y"))
    targetLocation = [targetInput[0], targetInput[2]]

    Matrix[int(targetLocation[0])][int(targetLocation[1])] = 3

    blockAmount = int(input("input BLOCK AMOUNT"))
    for block in range(blockAmount):
        blockInput = str(input("input BLOCK LOCATION in the format of x,y"))
        blockLocation = [blockInput[0],blockInput[2]]
        Matrix[int(blockLocation[0])][int(blockLocation[1])] = 1


    display(Matrix)




    endInput = input("end.")

main()