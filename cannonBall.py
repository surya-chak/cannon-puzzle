import numpy as np
import copy
import os

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
        newEnemy = np.random.randint(2, size=self.nCol)
        # Need a little more work here ... after a few levels:
        # The number of enemies generated should be higher
        return newEnemy

    def step(self):             # Enemies take one step forward
        if (sum(self.gameGrid[-1, :]) > 0):
            os.system('clear')
            print(self.gameGrid)
            print()
            print(self.cannonState)
            print()
            print(f"Available cannnon {self.availCannon}")
            print("you lost... sorry")
            exit
        else:
            self.gameGrid[1:self.nRow-1, :] = self.gameGrid[0: self.nRow-2, :]
            self.gameGrid[0, :] = self.makeEnemy()  # Random innitialization
            os.system('clear')
            print(self.gameGrid)
            print()
            print(self.cannonState)
            print()
            print(f"Available cannnon {self.availCannon}")

    def fire(self):             # damage calculation for cannon shots
        tempCannonState = copy.copy(self.cannonState)
        for j in range(self.nRow - 1, -1, -1):
            # print(j)
            # print(self.nRow)
            tempRow = copy.copy(self.gameGrid[j, :])  # Save state before hit
            # Hit
            self.gameGrid[j, :] -= (tempRow != 0) * tempCannonState[:]
            
            # reduce cannonState
            tempCannonState -= tempRow

            # Check if cannon state Negative
            tempCannonState = (tempCannonState > 0) * tempCannonState
            # Check for overHits: hit with more cannon than enemy
            # In this case the tempCannonState goes to zero
            tempCannonState -= (self.gameGrid[j, :] < 0) * tempCannonState

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