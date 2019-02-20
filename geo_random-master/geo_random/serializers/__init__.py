from .base import *
from .pickle_serializer import *


SERIALIZERS = {
    'pickle': PickleShapeSerializer
}

_default_serializer = 'pickle'


def get_serializer(alias=None):
    serializer = SERIALIZERS.get(alias or _default_serializer)
    return serializer
