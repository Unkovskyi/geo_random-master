"""
Модуль, в якому описані основні класи для побудови кола, трикутника, прямокутника:точка, лінія, а також медоди роботи з ними
"""

from math import sqrt
from  string import ascii_uppercase
from geo_random.exceptions import InvalidLineException, MaxPointCountExceeded, BaseShapeException



class Point:
    """
    Клас точка
    """

    def __init__(self, x, y):
        """
        Коструктор класу, об'єкт з атрибутами х та у
        """

        self.x = x
        self.y = y

    def __str__(self):
        """
        Представлення об'єкта класу в строковому вигляді
        """
        return ('{};{}'.format(self.x,self.y))


    def __eq__(self, other):
        assert isinstance(other, Point)
        result=(self.x==other.x and self.y==other.y)
        return result


class Line:
    """
    Клас лініяю Клас приймає два об'єкта класу Point
    """

    def __init__(self, p1, p2):
        """
        Коструктор класу об'єкт з атрибутами р1 та р2 класу Point
        """

        self.p1 = p1
        self.p2 = p2
        self.is_valid()

    def __str__(self):
        """
        Представлення об'єкта класа в строковому вигляді
        """
        return '(A{},B{})'.format(self.p1,self.p2)
        #return f'A{self.p1},B{self.p2}' #інший спосіб

    def is_valid(self):
        """
        Метод класу Line що перевіряє що точки не співпадають
        """
        if self.p1==self.p1:
        #if self.p1.x == self.p2.x and self.p1.y == self.p2.y:
            raise InvalidLineException('P1{} and P2{} are identical'.format(self.p1, self.p2))




    def get_distance(self):
        """
        Метод класу Line що по факту повертає відстань між точками
        """
        x = self.p1.x - self.p2.x
        y = self.p1.y - self.p2.y
        result = sqrt(x ** 2 + y ** 2)

        return result

    @property
    def distance(self):
        """
        Метод класу Line що повертає функцію get_distance а декоратор @property дозволяэ це робити без дужок
        """

        return self.get_distance()


class BaseShape:
    """
    Базовий клас
    """

    max_points = 0

    def __init__(self, points=None):

        """
        Коструктор класу об'єкт з атрибутами точки та лінії а також методом is_valid
        """

        self.points = points or list()
        self.lines = list()
        self.is_valid()

    # def __str__(self):
    #     return ', '.join(self.points.__str__())


    def add_point(self, point):
        """
        Метод класу BaseShape, що додає точку та вставляє її у список при цьому перевіряє чи співпадають точки
        """
        self.points.append(point)

        try:
            self.is_valid()
        except BaseShapeException as e:
            self.points.remove(point)
            raise e

    def is_valid(self):
        """
        Перевизначення методу is_valid який переіряє що фігура коректна
        """
        if len(self.points) > self.max_points:
            raise MaxPointCountExceeded('Allowed {} but got {}'.format(self.max_points, len(self.points)))

        return True

    def get_square(self):
        """
        Метод класу BaseShape для визначення площі фігури
        """
        raise NotImplementedError()

    def build_lines(self):
        """
        Метод класу BaseShape для створення лінії
        """

        raise NotImplementedError()

    def __str__(self):
        """
        Представлення об'єкта класа в строковому вигляді
        """
        result=' '
        point_string=[str(p) for p in self.points]
        point_with_letter=[]
        for idx,p in enumerate(point_string):
            point_with_letter.append(ascii_uppercase[idx]+p)
            result=','.join(point_with_letter)
        return result