from cell import Cell
from grid import Grid, EAST, NORTH
from random import randint, choice
from typing import List


class Sidewinder:
    def __init__(self, grid: Grid) -> None:
        self.grid: Grid = grid

    def create(self):
        for row in self.grid.get_per_row():
            run: List[Cell] = []
            for cell in row:
                run.append(cell)

                at_rows_end = cell.get_neighbour(EAST) is None
                at_last_row = cell.get_neighbour(NORTH) is None

                end_current_run = at_rows_end or (
                    not at_last_row and randint(0, 1) == 0
                )

                if end_current_run:
                    random_cell = choice(run)
                    if random_cell.get_neighbour(NORTH) is not None:
                        random_cell.link(random_cell.get_neighbour(NORTH))
                    run = []
                else:
                    cell.link(cell.get_neighbour(EAST))

        return self.grid
