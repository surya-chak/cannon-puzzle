from cannonBall import Game
import curses


def c_main(stdcr: 'curses._CursesWindow') -> int:
    nRow = 10
    nCol = 6
    # create new game
    g = Game(nRow, nCol, stdcr)

    while True:
        g.step()
        fromCell, toCell = int(input()), int(input())
        g.moveCannon(fromCell, toCell)
        g.fire()

    return 0


def main() -> int:
    return curses.wrapper(c_main)


if __name__ == "__main__":
    main()
