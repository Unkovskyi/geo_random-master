"""
doc string goes here
"""

__all__ = ['PickleShapeSerializer']

# Standard library imports.
import pickle

# Related third party imports.

# Local application/library specific imports.
from .base import BaseShapeSerializer


class PickleShapeSerializer(BaseShapeSerializer):
    """
    Клас сералізації, десирилізації
    """

    def serialize_instance(self, shape_instance):
        """
        Метод класу для сералізації екземплару класу
        """
        return pickle.dumps(shape_instance)

    def deserializer_instance(self, shape_data):
        """
        Метод класу для десералізації екземплару класу
        """
        return pickle.loads(shape_data)
