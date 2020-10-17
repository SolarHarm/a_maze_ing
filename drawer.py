from dataclasses import dataclass
import png
from typing import List
from copy import deepcopy


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class OutsideCanvasError(Exception):
    pass


class NoColorError(Exception):
    pass


class Drawer:
    def __init__(
        self,
        width: int,
        height: int,
        black_white: bool = True,
        inverse_axis: bool = False,
    ) -> None:
        self._width = width
        self._height = height
        self._inverse_axis = inverse_axis
        self._black_white = black_white
        self._canvas: List[List[int]] = self._set_canvas(black_white)

    def _set_canvas(self, black_white: bool):
        if black_white:
            return [[255 for _ in range(self._width)] for _ in range(self._height)]
        else:
            raise NotImplementedError

    def save_to_png(self, filename: str):
        with open(filename, "wb") as f:  # binary mode is important
            w = png.Writer(self._width, self._height, greyscale=True)
            w.write(f, self._canvas)

    def get_canvas(self):
        """ Returns copy of canvas"""

        return deepcopy(self._canvas)

    def get_point_on_canvas(self, point: Point):

        if self._inverse_axis:
            y = self._height - 1 - point.y
            return self._canvas[y][point.x]

        return self._canvas[point.y][point.x]

    def points_on_canvas(self, points: List[Point], exception_raised: bool = True):
        if exception_raised:
            for p in points:
                self.point_on_canvas(p, exception_raised=exception_raised)

        return [self.point_on_canvas(p) for p in points]

    def point_on_canvas(self, p: Point, exception_raised: bool = True):
        if p.x >= self._width:
            if exception_raised:
                raise OutsideCanvasError("Point x value outside canvas")
            return False

        if p.y >= self._height:
            if exception_raised:
                raise OutsideCanvasError("Point y value outside canvas")
            return False

        return True

    def paint_point(self, p: Point):
        self.point_on_canvas(p)
        self._paint_point(p.x, p.y)

    def paint_line(self, point1: Point, point2: Point):
        self.points_on_canvas([point1, point2])

        if point1.y == point2.y:
            self._paint_horizontal_line(point1.x, point2.x, point1.y)
        elif point1.x == point2.x:
            self._paint_vertical_line(point1.y, point2.y, point1.x)
        else:
            raise NotImplementedError("Can only paint horizontal or vertical lines")

    def _paint_horizontal_line(self, x1: int, x2: int, y: int):
        if x1 > x2:
            x1, x2 = x2, x1

        for x in range(x1, x2):
            self._paint_point(x, y)

    def _paint_vertical_line(self, y1: int, y2: int, x: int):
        if y1 > y2:
            y1, y2 = y2, y1

        for y in range(y1, y2):
            self._paint_point(x, y)

    def _paint_point(self, x: int, y: int, color: int = None):
        if color is None:
            if self._black_white:
                color = 0
            else:
                raise NoColorError("Please supply a color")

        if self._inverse_axis:
            y = self._height - 1 - y

        self._canvas[y][x] = color

    def _print(self):
        print("From Drawer _print")
        import pprint

        pprint.pprint(self._canvas)

