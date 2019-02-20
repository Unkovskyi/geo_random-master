"""
doc string goes here
"""

__all__ = ['STORAGE_DIR', 'DEFAULT_SERIALIZER']

# Standard library imports.
from pathlib import Path

# Related third party imports.

# Local application/library specific imports.


STORAGE_DIR = Path.joinpath(Path(__file__).resolve().parent.parent, 'var/shapes')
DEFAULT_SERIALIZER = 'pickle'

if not STORAGE_DIR.exists():
    Path(STORAGE_DIR).mkdir(parents=True)

STORAGE_DIR = str(STORAGE_DIR)
