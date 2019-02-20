"""
doc string goes here
"""

__all__ = ['SimpleConsoleCommand']

# Standard library imports.

# Related third party imports.

# Local application/library specific imports.
from geo_random.shapes import *
from geo_random.config import DEFAULT_SERIALIZER, STORAGE_DIR
from geo_random.serializers import get_serializer
from .base import BaseConsoleCommand


SHAPES = {
    'triangle': TriangleShape,
    'square': SquareShape,
    'circle': CircleShape
}


class SimpleConsoleCommand(BaseConsoleCommand):
    command_name = 'simple'

    def __init__(self, console_args):
        super().__init__(console_args)
        self.shape_type = console_args[0]
        self.points = console_args[1:]
        self.serializer_cls = get_serializer(DEFAULT_SERIALIZER)

    def run(self):
        if self.shape_type not in SHAPES:
            raise Exception('Invalid shape type')

        shape_cls = SHAPES[self.shape_type]

        def map_pints(p):
            x, y = p.split(',')
            return float(x), float(y)

        points = map(map_pints, self.points)
        points = [Point(*p) for p in points]

        shape = shape_cls(points=points)

        serializer = self.serializer_cls(STORAGE_DIR, [shape])
        serializer.store()

        return shape.get_square()
