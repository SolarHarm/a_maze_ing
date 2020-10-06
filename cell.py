from dataclasses import dataclass
from typing import List, Optional, Dict


class NeighbourError(Exception):
    pass


@dataclass(frozen=True)
class Position:
    row: int
    column: int


class Cell:
    """
    A cell is part of a grid, a cell has neighbours to the north, south, east
    and west unless it is a boundary cell.

    """

    def __init__(self, position: Position,) -> None:
        self._position: Position = position
        self._linked: List[Cell] = []

        self._neighbours: Dict[str, Position]

    @property
    def get_position(self):
        return self._position

    def link(self, other_cell: "Cell", both: bool = True):
        self._linked.append(other_cell)
        if both:
            other_cell.link(self, False)

    def unlink(self, other_cell: "Cell", both: bool = True):
        self._linked.remove(other_cell)
        if both:
            other_cell.unlink(self, False)

    def get_links(self):
        return self._linked

    def is_linked_with(self, other_cell: "Cell"):
        return other_cell in self._linked

    def get_neighbours(self):
        return self._neighbours.values()

    def set_neighbour(self, side: str, position: Position):
        if side not in ["north", "east", "south", "west"]:
            raise NeighbourError("Not in the windroos")

        self._neighbours[side] = position

    def cell_at_position(self, position: Position) -> bool:
        return self._position == position
