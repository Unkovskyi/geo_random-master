from .base import *
from .deserialize import *
from .simple import *


COMMANDS = {
    SimpleConsoleCommand.command_name: SimpleConsoleCommand,
    DeserializeConsoleCommand.command_name: DeserializeConsoleCommand
}
