"""Core kinkajou objects
This module contains the core objects for the kinkajou library

Todo:
    Write Todo
"""


from __future__ import annotations
from typing import Callable


class KinkajouClass:
    """Base Class for other kinkajou Classes"""


class DataCage(KinkajouClass):
    """DataCage object"""

    def __init__(self: DataCage, header: list, data: list) -> None:
        self._header = header
        self._data = data

    def __str__(self: DataCage) -> str:
        raise NotImplementedError

    def __repr__(self: DataCage) -> str:
        raise NotImplementedError

    def __len__(self: DataCage) -> int:
        return len(self._data)

    @property
    def header(self: DataCage) -> list:
        """Return list of headers"""
        return self._headers

    @header.setter
    def header(self: DataCage, newheader: list) -> None:
        """
        Todo: Write this function so that
        if: len(self._header) = len(newheader) - then set them
        if: len(self._header) < len(newheader) - then add empty values to each row
        if: len(self._header) > len(newheader) -
            if right column(s) are empty - remove them
            else raise error (can-not delete non-empty columns through setting headers)
        """
        self._headers = newheader

    # @property
    def column(self: DataCage, column: int | str = 0) -> list:
        """Return a list containing all values from a column

        Args:
            column (int | str): either index or header of column to fetch

        Returns:
            list: list of values from column
        """

    # @column.setter
    # def column(self: DataCage, column: int|str = 0, values: list) -> None:

    def modify_column(self: DataCage, column: int | str, operation: Callable) -> None:
        """Modify a column in the datacage through provided Lambda function

        Args:
            Column (int | str): either index or header of column to modify
            operation (Callable): lambda function to map to column
        """
