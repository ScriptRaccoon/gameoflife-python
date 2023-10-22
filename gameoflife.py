"""
Game of Life Simulation in the console
"""

# pylint: disable=missing-function-docstring

import os
import time
import random
from typing import Literal, cast

SIZE_X = 60
"""size of the game in x-direction"""

SIZE_Y = 30
"""size of the game in y-direction"""

LIVE_TO_LIVE = [2, 3]
"""number of living neighbors required for a living cell to live on"""

DEAD_TO_LIVE = [3]
"""number of living neighbors required for a dead cell to become alife"""

CELL_SYMBOLS = ["  ", "■ "]
"""symbols used for printing the cell (dead or alife)"""

Binary = Literal[0, 1]
"""Type of a binary number: 0 or 1"""

BinaryMatrix = list[list[Binary]]
"""Type of a 2-dimensional array with entries only 0 or 1"""

Coordinate = tuple[int, int]
"""Type of a 2-dimensional coordinate"""


def clear_console() -> None:
    clear_command = "cls" if os.name == "nt" else "clear"
    os.system(clear_command)


def get_empty_cells() -> BinaryMatrix:
    return [[0 for _ in range(SIZE_Y)] for _ in range(SIZE_X)]


def get_random_cells() -> BinaryMatrix:
    return [
        [cast(Binary, random.randint(0, 1)) for _ in range(SIZE_Y)]
        for _ in range(SIZE_X)
    ]


def print_cells(cells: BinaryMatrix) -> None:
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            cell = cells[x][y]
            print(CELL_SYMBOLS[cell], end="")
        print()


def get_living_neighbors(
    cells: BinaryMatrix, coordinate: Coordinate
) -> list[Coordinate]:
    x, y = coordinate
    all_coordinates = [(x + i, y + j) for i in [-1, 0, +1] for j in [-1, 0, +1]]

    def is_living(coord: Coordinate):
        u, v = coord
        return (
            0 <= u < SIZE_X
            and 0 <= v < SIZE_Y
            and (u, v) != (x, y)
            and cells[u][v] == 1
        )

    return list(filter(is_living, all_coordinates))


def get_next_cells(cells: BinaryMatrix) -> BinaryMatrix:
    next_cells = get_empty_cells()
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            cell = cells[x][y]
            amount_living_neighbors = len(get_living_neighbors(cells, (x, y)))
            if cell == 1:
                next_cells[x][y] = 1 if amount_living_neighbors in LIVE_TO_LIVE else 0
            else:
                next_cells[x][y] = 1 if amount_living_neighbors in DEAD_TO_LIVE else 0
    return next_cells


def main() -> None:
    cells = get_random_cells()
    while True:
        clear_console()
        print_cells(cells)
        time.sleep(0.5)
        cells = get_next_cells(cells)


if __name__ == "__main__":
    main()
