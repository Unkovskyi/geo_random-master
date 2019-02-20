'''Модуль для обробки помилок'''

class BaseShapeException(Exception):
    '''Клас для обробки базових помилок що наслідує клас Exception'''

    default_message = 'There was an exception'

    def __init__(self, message=None, *args, **kwargs):
        self.message = message or self.default_message

    def __str__(self):
        return self.message


class InvalidLineException(BaseShapeException):
    """
    Клас що наслідує клас BaseShapeException для обробки помилок повязаних з побудовою лінії
    """

    default_message = 'Invalid line: point are the same'


class MaxPointCountExceeded(BaseShapeException):
    """
    Клас що наслідує клас BaseShapeException для перевірки кількості точок для побудови фігури
    """
    default_message = 'Maximum point of lines was exceeded'


class InvalidCircleException(BaseShapeException):
    """
    Клас що наслідує клас BaseShapeException для перевірки коректності побудови кола
    """

    default_message = 'Invalid circle exception'


class InvalidSquareException(BaseShapeException):
    """
    Клас що наслідує клас BaseShapeException для перевірки коректності побудови прямокутника
    """

    default_message = 'Invalid square exception'
