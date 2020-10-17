from generics.drawer import Drawer, Point
import random
from typing import List


from generics.cell import Cell, Position

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

        # TODO Allow to change
        self.open_h = "   "
        self.open_v = " "
        self.corner = "+"
        self.wall_v = "|"
        self.wall_h = "---"

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

    # Private below don't call directly
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

    def to_png(self):
        cell_dim = 10
        height_px = self.rows * cell_dim + 1
        width_px = self.columns * cell_dim + 1

        drawer = Drawer(width_px, height_px)
        print("here")
        for cell in self.get_per_cell():
            x, y = cell.get_position.column * cell_dim, cell.get_position.row * cell_dim

            tl = Point(x, y)
            tr = Point(x + cell_dim, y)
            bl = Point(x, y + cell_dim)
            br = Point(x + cell_dim, y + cell_dim)

            if cell.has_wall_at(NORTH):
                drawer.paint_line(tl, tr)
            if cell.has_wall_at(EAST):
                drawer.paint_line(tr, br)
            if cell.has_wall_at(SOUTH):
                drawer.paint_line(bl, br)
            if cell.has_wall_at(WEST):
                drawer.paint_line(tl, bl)

        print("here alreadu")

        drawer.save_to_png("test.png")
