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

        self.size = len(self.grid)

    def _prepare_grid(self):
        return [
            Cell(Position(row, column))
            for row in range(self.rows)
            for column in range(self.columns)
        ]

    def _set_neighbour(self, cell: Cell, side: str, position: Position):
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

    def get_per_row(self):
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
        # Build ascii art
        # +---+---+---+
        # |   |   |   |
        # +---+---+---+
        # |   |   |   |
        # +---+---+---+
        #  We start with '+' + '---+' * cols
        #  each row start with '|' + ['   ' + ' ' || '|'] -> for each cell
        #  each row also has   '+' + ['---+'] -> for each cell

        top_s = "+" + "---+" * self.columns + "\n"
        for row in self.get_per_row():
            row_s = "|"
            bottom_s = ""
            for cell in row:
                row_s += "   " + (
                    " " if cell.is_linked_with(cell.get_neighbour(EAST)) else "|"
                )
                bottom_s += "+" + (
                    "   " if cell.is_linked_with(cell.get_neighbour(SOUTH)) else "---"
                )
            top_s += row_s + "\n" + bottom_s + "+\n"

        return top_s

