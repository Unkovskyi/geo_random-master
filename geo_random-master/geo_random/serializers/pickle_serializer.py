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

    def serialize_instance(self, shape_instance):
        return pickle.dumps(shape_instance)

    def deserializer_instance(self, shape_data):
        return pickle.loads(shape_data)
