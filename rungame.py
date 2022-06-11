from cannonBall import Game

nRow = 10
nCol = 6
maxEnemy = 6
# create new game
g = Game(nRow, nCol, maxEnemy)

# test section
# g.step()
# g.step()
# g.step()

# g.moveCannon(99, 1)
# g.moveCannon(99, 1)
# g.moveCannon(99, 1)
# g.moveCannon(99, 1)
# g.moveCannon(99, 1)


# g.fire()
# print(g.gameGrid)
# print()
# print(g.cannonState)
# g.fire()
# print(g.gameGrid)
# print()
# print(g.cannonState)
# g.fire()
# print(g.gameGrid)
# print()
# print(g.cannonState)

# start game loop
while True:
    g.step()
    fromCell, toCell = int(input()), int(input())
    g.moveCannon(fromCell, toCell)
    gameGrid = g.fire()
