
"""
Модуль, в якому описана фігура коло та знаходження її площі
"""

from math import pi
from geo_random.shapes.base import BaseShape, Line, Point
from geo_random.exceptions import InvalidCircleException


class CircleShape(BaseShape):
    """
    Клас Коло
    """

    max_points = 2

    def __init__(self, points=None):
        """
        Конструктор класу який використовує метод build_lines класу BaseShape для побудови лінії
        """
        super().__init__(points)
        self.build_lines()

    def add_point(self, point):
        """
        Метод класу який використовує метод add_point класу BaseShape для додавання точки та побудови лінії
        """
        super().add_point(point)
        self.build_lines()

    def is_valid(self):
        """
        Метод класу який використовує метод is_valid класу BaseShape для перевірки коректності побудови фігури        Метод класу який використовує метод add_point класу BaseShape для додавання точки та побудови лінії
        """
        super().is_valid()
        if len(self.points) == self.max_points:
            p1, p2 = tuple(self.points)
            if p1.x == p2.x and p1.y == p2.y:
                raise InvalidCircleException('Points P1{} and P2{} are similar'.format(p1, p2))

    def get_square(self):
        """
        Метод класу  для розрахунку площі кола
        """
        self.build_lines()
        line = self.lines[0]
        return pi * line.get_distance()

    def build_lines(self):
        """
        Метод класу  побудови лінії
        """
        if len(self.points) == self.max_points:
            self.lines = list()
            line = Line(*self.points)
            self.lines.append(line)