from cannonBall import Game

nRow = 10
nCol = 6
maxEnemy = 6
# create new game
g = Game(nRow, nCol, maxEnemy)

# start game loop
while True:
    g.step()
    fromCell, toCell = int(input()), int(input())
    g.moveCannon(fromCell, toCell)
    gameGrid = g.fire()
