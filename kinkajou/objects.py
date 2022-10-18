"""Core kinkajou objects
This module contains the core objects for the kinkajou library

Todo:
    Write Todo
"""


from __future__ import annotations

from kinkajou.errors import CagingError


class DataCage:
    """_summary_"""

    def __init__(self: DataCage, thing) -> None:
        raise CagingError

    def __str__(self: DataCage) -> str:
        raise NotImplementedError

    def __repr__(self: DataCage) -> str:
        raise NotImplementedError

    def __len__(self: DataCage) -> int:
        raise NotImplementedError

    def __add__(self: DataCage, other: DataCage) -> DataCage:
        raise NotImplementedError
