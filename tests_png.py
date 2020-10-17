import unittest
import png
import grid
import cell
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


from pprint import pprint


class TestPNGModule(unittest.TestCase):
    def setUp(self) -> None:
        self.width, self.height = 10, 10
        self.canvas = [[255 for _ in range(self.width)] for _ in range(self.height)]

    def test_draw_h_line(self):
        # draw horizontal line at +5 pixels from bottom
        at_y: int = 4

        p1 = Point(0, at_y)
        p2 = Point(self.width, at_y)

        for x in range(p2.x - p1.x):
            self.canvas[p2.y][x] = 0

        self.assertListEqual(
            self.canvas,
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255,],
            ],
        )
        with open(f"test_h.png", "wb") as f:  # binary mode is important
            w = png.Writer(self.width, self.height, greyscale=True)
            w.write(f, self.canvas)

    def test_draw_v_line(self):
        # draw vertical line at +5 pixels from left
        at_x: int = 4

        p1 = Point(at_x, 0)
        p2 = Point(at_x, self.height)

        for y in range(p2.y - p1.y):
            self.canvas[y][p2.x] = 0

        self.assertListEqual(
            self.canvas,
            [
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
                [255, 255, 255, 255, 0, 255, 255, 255, 255, 255,],
            ],
        )
        with open(f"test_name_v.png", "wb") as f:  # binary mode is important
            w = png.Writer(self.width, self.height, greyscale=True)
            w.write(f, self.canvas)


if __name__ == "__main__":
    unittest.main()
