"""
doc string goes here
"""

__all__ = ['BaseConsoleCommand']

# Standard library imports.

# Related third party imports.

# Local application/library specific imports.


class BaseConsoleCommand:
    command_name = None

    def __init__(self, console_args):
        assert self.command_name is not None, '`command_name` must be specified'
        self.console_args = console_args

    def run(self):
        raise NotImplementedError()
