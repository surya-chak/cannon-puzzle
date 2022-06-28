import numpy as np
import copy
# import os
import random
import math
import curses


class Game:

    def __init__(self,
                 nRow,
                 nCol):
        # stdscr: curses.window
        """
        Class that defines the game, and some basic setup parameters like:
        - Number of Columns
        - Number of Row
        - Max Enemy generation at each step
        """
        self.nRow = nRow
        self.nCol = nCol
        # self.maxEnemy = maxEnemy
        # self.stdscr = stdscr
        self.stdscr = curses.initscr()
        curses.curs_set(0)
        curses.mousemask(-1)
        # curses.mouseinterval(0)
        self.stdscr.keypad(1)

        self.gameGrid = np.zeros((nRow, nCol)).astype(int)
        self.cannonState = np.zeros(nCol).astype(int)
        self.availCannon = 0
        self.gameCounter = 0

    def printState(self):
        self.stdscr.erase()
        self.stdscr.refresh()
        # Adding the gameGrid display
        for iCol in range(self.nCol):
            for jRow in range(self.nRow):
                self.stdscr.addstr(3 * jRow+2,
                                   8 * iCol+2,
                                   str(self.gameGrid[jRow, iCol]))

        # Adding the cannon state Display
        for iCol in range(self.nCol):
            self.stdscr.addstr(3 * self.nRow + 6,
                               8 * iCol + 2,
                               str(self.cannonState[iCol]))

        # Adding the available cannon display
        self.stdscr.addstr(3 * self.nRow + 10,
                           8 * int(self.nCol / 2) - 1,
                           str(self.availCannon))

    def printLoss(self):
        self.stdscr.refresh()
        self.stdscr.erase()
        self.stdscr.addstr('you lost ... sorry')

    def rounddown(self, x):
        return int(math.ceil(x / 1.0)) * 1

    def makeEnemy(self):
        totals = [self.rounddown(self.gameCounter/3)]
        newEnemy = []
        for i in totals:
            if i == 0:
                newEnemy.append([0 for i in range(self.nCol)])
                continue
            total = i
            temp = []
            for i in range(self.nCol-1):
                val = np.random.randint(0, total)
                temp.append(val)
                total -= val
            temp.append(total)
            newEnemy.append(temp)

        return np.array(newEnemy)

    def step(self):             # Enemies take one step forward
        if (sum(self.gameGrid[-1, :]) > 0):
            # os.system('clear')
            self.printState()
            self.printLoss()
            exit
        else:
            self.gameCounter += 1
            self.gameGrid[1:self.nRow-1, :] = self.gameGrid[0: self.nRow-2, :]
            self.gameGrid[0, :] = self.makeEnemy()  # Random innitialization
            self.printState()

    def fire(self):             # damage calculation for cannon shots
        tempCannonState = copy.copy(self.cannonState)
        for j in range(self.nRow - 1, -1, -1):
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

    def getInput(self):
        fromState = 0
        toState = 0
        x, y = 0, 0
        # pressed = False
        # determining the to state
        while True:
            c = self.stdscr.get_wch()
            if c == 'q':
                exit
            elif c == curses.KEY_MOUSE:
                _, x, y, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON1_PRESSED:
                    # Visual for button being pressed
                    for y_val in range(y-1, y+2):
                        self.stdscr.addstr(y_val, x - 1, 'XXX')

                    # Check if additional cannon button pressed
                    if ((3 * self.nRow + 9) < y < (3 * self.nRow + 11) and
                            (8 * int(self.nCol / 2) - 2) < x < 8 * int(self.nCol / 2)):
                        fromState = 99
                        if self.availCannon == 0:
                            toState = 0
                            self.moveCannon(fromState, toState)
                            return

                    elif ((3 * self.nRow + 5) < y < (3 * self.nRow + 7)):
                        fromState = int((x-2)/8)
                    else:
                        continue
                # elif bstate & curses.BUTTON1_RELEASED:
                #     self.stdscr.erase()
                #     self.printState()
                    break               # one of the buttons were clicked correctly

        # Determining the to state
        x, y = 0, 0
        while True:
            c = self.stdscr.get_wch()
            if c == 'q':
                exit
            elif c == curses.KEY_MOUSE:
                _, x, y, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON1_PRESSED:
                    # Visual for button being pressed
                    for y_val in range(y-1, y+2):
                        self.stdscr.addstr(y_val, x - 1, 'XXX')

                    # Check if additional cannon button pressed
                    if ((3 * self.nRow + 5) < y < (3 * self.nRow + 7)):
                        toState = int((x-2)/8)
                    else:
                        continue

                # elif bstate & curses.BUTTON1_RELEASED:
                #     self.stdscr.erase()
                #     self.printState()
                    break     # none of the buttons were clicked correctly
        self.moveCannon(fromState, toState)
