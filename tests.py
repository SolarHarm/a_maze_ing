from binary_tree import BinaryTree
from cell import Cell, Position
from grid import Grid, NORTH, EAST, SOUTH, WEST

import unittest


class TestCell(unittest.TestCase):
    def setUp(self) -> None:
        self.row, self.column = 4, 7
        self.other_cell = Cell(Position(3, 7))
        self.position = Position(self.row, self.column)
        self.cell = Cell(self.position)

    def test_get_position(self):
        self.assertEqual(self.cell.get_position, self.position)

    def test_link_both(self):
        self.cell.link(self.other_cell)

        self.assertListEqual([self.other_cell], self.cell._linked)
        self.assertListEqual([self.cell], self.other_cell._linked)

    def test_only_link_one(self):
        self.cell.link(self.other_cell, both=False)

        self.assertListEqual([self.other_cell], self.cell._linked)
        self.assertListEqual([], self.other_cell._linked)

    def test_is_linked_with(self):
        self.cell.link(self.other_cell)

        self.assertTrue(self.cell.is_linked_with(self.other_cell))
        self.assertTrue(self.other_cell.is_linked_with(self.cell))

    def test_set_neighbours(self):
        self.cell.set_neighbour(NORTH, self.other_cell)
        self.cell.set_neighbour(EAST, self.other_cell)
        self.cell.set_neighbour(SOUTH, self.other_cell)
        self.cell.set_neighbour(WEST, self.other_cell)

        self.assertEqual(
            list(self.cell.get_neighbours().values()),
            [self.other_cell, self.other_cell, self.other_cell, self.other_cell],
        )
        self.assertEqual(self.cell.get_neighbour(NORTH), self.other_cell)
        self.assertEqual(self.cell.get_neighbour(EAST), self.other_cell)
        self.assertEqual(self.cell.get_neighbour(SOUTH), self.other_cell)
        self.assertEqual(self.cell.get_neighbour(WEST), self.other_cell)

    def test_cell_at_position(self):
        position = Position(self.row, self.column)
        not_position = Position(self.row + 1, self.column)

        self.assertTrue(self.cell.at_position(position))
        self.assertFalse(self.cell.at_position(not_position))


class TestGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = 2
        self.columns = 3

        self.grid = Grid(self.rows, self.columns)

    def test_size(self):
        self.grid.size = self.rows * self.columns

    def test_prepare_grid(self):
        self.assertEqual(
            repr(self.grid),
            (
                "[Cell at (0,0), Cell at (0,1), Cell at (0,2)]\n"
                "[Cell at (1,0), Cell at (1,1), Cell at (1,2)]"
            ),
        )

    def test_get_randmon_cell(self):
        self.assertTrue(isinstance(self.grid.get_random_cell(), Cell))

    def test_get_per_row(self):
        rows = self.grid.get_per_row()

        for col, cell in enumerate(next(rows)):
            self.assertEqual(cell.get_position.row, 0)
            self.assertEqual(cell.get_position.column, col)
        for col, cell in enumerate(next(rows)):
            self.assertEqual(cell.get_position.row, 1)
            self.assertEqual(cell.get_position.column, col)

    def test_grid_string(self):
        pass


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        grid = Grid(10, 10)
        self.bt = BinaryTree(grid)

    def test_create(self) -> None:
        assert self.bt.create() != None


if __name__ == "__main__":
    unittest.main()
