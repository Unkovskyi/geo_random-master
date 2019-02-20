"""
doc string goes here
"""

__all__ = ['BaseShapeSerializer']

# Standard library imports.
import os
from os import path

# Related third party imports.

# Local application/library specific imports.


class BaseShapeSerializer:
    file_extension = 'default'

    def __init__(self, dir_path, shapes):
        if not path.exists(dir_path):
            raise Exception('Path does not exist')

        if not path.isdir(dir_path):
            raise Exception('Path is not dir')

        self.dir_path = dir_path
        self.shapes = shapes

    def store(self):
        for idx, shape in enumerate(self.shapes):
            file_name = self.generate_file_name(shape, idx)
            serialized_shape = self.serialize_instance(shape)

            full_path = path.join(self.dir_path, file_name)

            with open(full_path, 'wb') as f:
                f.write(serialized_shape)

    def restore(self):
        result = []

        for file_name in os.listdir(self.dir_path):
            full_path = path.join(self.dir_path, file_name)

            if not path.isfile(full_path):
                continue

            with open(full_path, 'rb') as f:
                shape_bytes = f.read()

            shape = self.deserializer_instance(shape_bytes)
            result.append(shape)

        return result

    def serialize_instance(self, shape_instance):
        raise NotImplementedError()

    def deserializer_instance(self, shape_data):
        raise NotImplementedError()

    def generate_file_name(self, shape, idx):
        class_name = type(shape).__name__
        file_name = '{class_name}_{idx}.{extension}'.format(class_name=class_name, idx=idx, extension=self.file_extension)
        return file_name
