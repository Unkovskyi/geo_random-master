"""
doc string goes here
"""

__all__ = ['BaseConsoleCommand']

# Standard library imports.

# Related third party imports.

# Local application/library specific imports.


class BaseConsoleCommand:

    """
    Клас для базових команд конслоі, що в конструкторі отримує команди, як аргументи, перевіряє їх на корректність
    """

    command_name = None

    def __init__(self, console_args):
        assert self.command_name is not None, '`command_name` must be specified'
        self.console_args = console_args

    def run(self):
        """
        Перевірка на помилки, щодо коректності введених в конслоь даних
        """
        raise NotImplementedError()
