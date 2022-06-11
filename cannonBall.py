import numpy as np
import copy


class Game:

    def __init__(self, nRow, nCol, maxEnemy):
        """
        Class that defines the game, and some basic setup parameters like:
        - Number of Columns
        - Number of Row
        - Max Enemy generation at each step
        """
        self.nRow = nRow
        self.nCol = nCol
        self.maxEnemy = maxEnemy
        self.gameGrid = np.zeros((nRow, nCol)).astype(int)
        self.cannonState = np.zeros(nCol).astype(int)
        self.availCannon = 0

    def makeEnemy(self):
        newEnemy = np.random.randint(2, size=nCol)
        # Need a little more work here ... after a few levels:
        # The number of enemies generated should be higher
        return newEnemy

    def step(self):             # Enemies take one step forward
        if (sum(self.gameGrid[-1, :]) > 0):
            print("you lost... sorry")
            print(self.gameGrid)
            print()
            print(self.cannonState)
            exit
        else:
            self.gameGrid[1:-1, :] = self.gameGrid[0: nRow-2, :]
            self.gameGrid[0, :] = self.makeEnemy()  # Random innitialization
            print(self.gameGrid)
            print()
            print(self.cannonState)

    def fire(self):             # damage calculation for cannon shots
        tempCannonState = copy.copy(self.cannonState)
        for j in range(self.nRow - 1, -1, -1):
            # print(j)
            # print(self.nRow)
            tempRow = copy.copy(self.gameGrid[j, :])  # Save state before hit
            # Hit
            self.gameGrid[j, :] += - tempCannonState[:]
            # reduce cannonState
            tempCannonState += - tempRow

            # Check if cannon state Negative
            tempCannonState = (tempCannonState > 0) * tempCannonState
            # Check for overHits: hit with more cannon than enemy
            # In this case the tempCannonState goes to zero
            tempCannonState += - (self.gameGrid[j, :] < 0) * tempCannonState

            # Check if Game Grid Negative
            self.gameGrid[j, :] = (self.gameGrid[j, :] > 0) * self.gameGrid[j, :]

            if (sum(tempCannonState) == 0):
                return

    def moveCannon(self, fromCell, toCell):
        if (fromCell == 99):
            if (self.availCannon > 0):
                self.availCannon = self.availCannon - 1
                self.cannonState[toCell] = self.cannonState[toCell] + 1
            else:
                self.availCannon = 1

        else:
            self.cannonState[toCell] = self.cannonState[toCell] + \
                self.cannonState[fromCell]
            self.cannonState[fromCell] = 0


nRow = 10
nCol = 6
maxEnemy = 6
# create new game
g = Game(nRow, nCol, maxEnemy)

# test section
g.step()
g.step()
g.step()

g.moveCannon(99, 1)
g.moveCannon(99, 1)
g.moveCannon(99, 1)
g.moveCannon(99, 1)
g.moveCannon(99, 1)


g.fire()
print(g.gameGrid)
print()
print(g.cannonState)
g.fire()
print(g.gameGrid)
print()
print(g.cannonState)
g.fire()
print(g.gameGrid)
print()
print(g.cannonState)

# Test commit by Sravya


# start game loop
# while True:
#     g.step()
#     move = input("Enter your move - ")
#     print(move)
#     cannonState, availCannon = g.moveCannon(move)
#     gameGrid = g.fire()
