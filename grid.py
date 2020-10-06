from cell import Cell, Position
import random

NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"


class Grid:
    """
    A grid contains all the cells
    """

    def __init__(self, rows: int, columns: int) -> None:
        self.rows: int = rows
        self.columns: int = columns

        self.grid = self._prepare_grid()
        self._configure_cells()

        self.size = self.rows * self.columns

    def _prepare_grid(self):
        return [
            Cell(Position(row, column))
            for row in range(self.rows)
            for column in range(self.columns)
        ]

    def _configure_cells(self):
        for cell in self.grid:
            row, column = cell.get_position

            if row - 1 >= 0:
                cell.set_neighbour(NORTH, Position(row - 1, column))
            if row + 1 < self.rows:
                cell.set_neighbour(SOUTH, Position(row + 1, column))
            if column - 1 >= 0:
                cell.set_neighbour(SOUTH, Position(row, column - 1))
            if column + 1 < self.column:
                cell.set_neighbour(SOUTH, Position(row, column + 1))

    def get_random_cell(self):
        row = random.randInt(0, self.rows - 1)
        column = random.randInt(0, self.columns - 1)
        return next(
            [cell for cell in self.grid if cell.cell_at_position(Position(row, column))]
        )

