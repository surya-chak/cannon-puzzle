from cannonBall import Game


def main():
    nRow = 8
    nCol = 6
    g = Game(nRow, nCol)

    while True:
        g.step()
        g.getInput()
        g.fire()

    return 0


if __name__ == "__main__":
    main()
