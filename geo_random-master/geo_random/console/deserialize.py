"""
doc string goes here
"""

__all__ = ['DeserializeConsoleCommand']

# Standard library imports.

# Related third party imports.

# Local application/library specific imports.
from geo_random.config import DEFAULT_SERIALIZER
from geo_random.serializers import get_serializer
from .base import BaseConsoleCommand


class DeserializeConsoleCommand(BaseConsoleCommand):
    command_name = 'deserialize'

    def __init__(self, console_args):
        super().__init__(console_args)
        self.dir_path = console_args[0]
        self.serializer_cls = get_serializer(DEFAULT_SERIALIZER)

    def run(self):
        serialize = self.serializer_cls(self.dir_path, None)
        shapes = serialize.restore()

        return shapes
