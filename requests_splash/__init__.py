import pathlib

from .session import Session


__version__ = (pathlib.Path(__file__).parent / 'VERSION').read_text().strip()
__all__ = [
    'Session',
]
