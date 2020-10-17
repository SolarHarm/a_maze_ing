import random
from typing import List

import png

from cell import Cell, Position

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

        self.size = len(self.grid)

        self.open_h = "   "
        self.open_v = " "
        self.corner = "+"
        self.wall_v = "|"
        self.wall_h = "---"

    def _prepare_grid(self):
        return [
            Cell(Position(row, column))
            for row in range(self.rows)
            for column in range(self.columns)
        ]

    def _set_neighbour(self, cell: Cell, side: str, position: Position) -> None:
        cell.set_neighbour(
            side, next((c for c in self.grid if c.at_position(position)), None,),
        )

    def _configure_cells(self):
        for cell in self.grid:
            row, column = cell.get_position.row, cell.get_position.column
            self._set_neighbour(cell, NORTH, Position(row - 1, column))
            self._set_neighbour(cell, SOUTH, Position(row + 1, column))
            self._set_neighbour(cell, WEST, Position(row, column - 1))
            self._set_neighbour(cell, EAST, Position(row, column + 1))

    def get_random_cell(self):
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return next(
            (cell for cell in self.grid if cell.at_position(Position(row, column)))
        )

    def get_per_row(self) -> List["Cell"]:
        for row in range(self.rows):
            yield sorted(
                [cell for cell in self.grid if cell.in_row(row)],
                key=lambda cell: cell.get_position.column,
            )

    def get_per_cell(self):
        for cell in self.grid:
            yield cell

    def __repr__(self):
        return "\n".join([str(row) for row in self.get_per_row()])

    def __str__(self):
        top_s = "\n " + self.corner + (self.wall_h + self.corner) * self.columns + "\n"
        for row in self.get_per_row():
            row_s = f"{row[0].get_position.row}{self.wall_v}"
            bottom_s = f" {self.corner}"
            for cell in row:
                self.open_h = f" {cell.get_position.column} "
                open_east = cell.is_linked_with(cell.get_neighbour(EAST))
                with_south = cell.is_linked_with(cell.get_neighbour(SOUTH))
                row_s += self.open_h + (self.open_v if open_east else self.wall_v)
                bottom_s += (self.open_h if with_south else self.wall_h) + self.corner

            top_s += "\n".join([row_s, bottom_s, ""])

        return top_s

    def to_png(self, name="maze"):
        cell_width = cell_height = 3
        width = self.columns * cell_width + 1
        height = self.rows * cell_height + 1

        canvas = [[255 for _ in range(width)] for _ in range(height)]

        for cell in self.get_per_cell():
            x1 = cell.get_position.column * cell_width
            y1 = cell.get_position.row * cell_height

            x2 = (cell.get_position.column + 1) * cell_width
            y2 = (cell.get_position.row + 1) * cell_height

            if cell.is_linked_with(cell.get_neighbour(SOUTH)):
                bottom = (x1, x2, y1)  # van, tot, hoogte
                for loc in range(bottom[0], bottom[1]):
                    canvas[bottom[2]][loc] = 0

            if cell.is_linked_with(cell.get_neighbour(NORTH)):
                top = (x1, x2, y2)
                for loc in range(top[0], top[1]):
                    canvas[top[2]][loc] = 0

            if cell.is_linked_with(cell.get_neighbour(WEST)):
                left = (x1, y1, y2)
                for loc in range(left[1], left[2]):
                    canvas[loc][left[0]] = 0

            if cell.is_linked_with(cell.get_neighbour(EAST)):
                right = (x2, y1, y2)
                for loc in range(right[1], right[2]):
                    canvas[loc][right[0]] = 0

        with open(f"{name}.png", "wb") as f:  # binary mode is important
            w = png.Writer(width, height, greyscale=True)
            w.write(f, canvas)

