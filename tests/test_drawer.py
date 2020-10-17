import unittest
from generics.drawer import Drawer, OutsideCanvasError, Point


class TestDrawer(unittest.TestCase):
    def setUp(self) -> None:
        self.height = 10
        self.width = 10

        self.drawer = Drawer(
            width=self.width, height=self.height, black_white=True, inverse_axis=True
        )

    def test_get_canvas_is_copy(self):
        copy = self.drawer.get_canvas()
        copy = []

        self.assertFalse(copy == self.drawer.get_canvas())

    def test_point_on_canvas(self):
        p1 = Point(5, 5)
        p2 = Point(10, 5)
        p3 = Point(5, 10)
        p4 = Point(9, 9)
        p5 = Point(10, 10)

        self.assertTrue(self.drawer.point_on_canvas(p1, exception_raised=False))
        self.assertFalse(self.drawer.point_on_canvas(p2, exception_raised=False))
        self.assertFalse(self.drawer.point_on_canvas(p3, exception_raised=False))
        with self.assertRaises(OutsideCanvasError):
            self.drawer.point_on_canvas(p5)

        self.assertTrue(self.drawer.point_on_canvas(p4))

    def test_paint_point(self):
        x: int = 0
        y: int = 9
        p = Point(x, y)

        self.drawer.paint_point(p)

        color = self.drawer.get_point_on_canvas(p)
        self.assertEqual(color, 0)

    def test_paint_horizontal_line(self):
        p1 = Point(2, 2)
        p2 = Point(9, 2)

        self.drawer.paint_line(p1, p2)

        canvas = self.drawer.get_canvas()
        self.assertEqual(
            canvas,
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 0, 0, 0, 0, 0, 0, 0, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            ],
        )

    def test_paint_vertical_line(self):
        p1 = Point(3, 2)
        p2 = Point(3, 9)

        self.drawer.paint_line(p1, p2)

        canvas = self.drawer.get_canvas()
        self.assertEqual(
            canvas,
            [
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 0, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
            ],
        )

    def _print(self, canvas):
        from pprint import pprint

        pprint(canvas)


if __name__ == "__main__":
    unittest.main()
