from generics.grid import Grid, NORTH, EAST
from random import choice as randChoice


class BinaryTree:
    """
    Create a new maze with the help of the binary tree method.
    """

    def __init__(self, grid: Grid):
        self.grid = grid

    def create(self) -> Grid:
        for cell in self.grid.get_per_cell():
            choices = [
                c
                for c in [cell.get_neighbour(NORTH), cell.get_neighbour(EAST)]
                if c != None
            ]
            if len(choices) != 0:
                cell.link(randChoice(choices))

        return self.grid
