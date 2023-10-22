"""
Game of Life Simulation in the console
"""

import os
import time
import random

SIZE_X = 50
SIZE_Y = 20


def clear_console() -> None:
    clear_command = "cls" if os.name == "nt" else "clear"
    os.system(clear_command)


def get_empty_cells() -> list[list[int]]:
    cells = []
    for _ in range(SIZE_X):
        row = []
        for _ in range(SIZE_Y):
            row.append(0)
        cells.append(row)
    return cells


def get_random_cells() -> list[list[int]]:
    cells = []
    for _ in range(SIZE_X):
        row = []
        for _ in range(SIZE_Y):
            row.append(random.randint(0, 1))
        cells.append(row)
    return cells


def cell_symbol(value: int) -> str:
    return " " if value == 0 else "o"


def print_cells(cells: list[list[int]]) -> None:
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            print(cell_symbol(cells[x][y]), end="")
        print("")


def get_living_neighbors(
    cells: list[list[int]], coordinate: tuple[int, int]
) -> list[tuple[int, int]]:
    x, y = coordinate
    all_coordinates = [
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    def allowed(coord: tuple[int, int]):
        u, v = coord
        return u >= 0 and u < SIZE_X and v >= 0 and v < SIZE_Y and cells[u][v] == 1

    return list(filter(allowed, all_coordinates))


def get_next_cells(cells: list[list[int]]) -> list[list[int]]:
    next_cells = get_empty_cells()
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            cell = cells[x][y]
            amount_living_neighbors = len(get_living_neighbors(cells, (x, y)))
            if cell == 1:
                next_cells[x][y] = 1 if amount_living_neighbors in [2, 3] else 0
            else:
                next_cells[x][y] = 1 if amount_living_neighbors == 3 else 0
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
