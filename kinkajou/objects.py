"""Core kinkajou objects
This module contains the core objects for the kinkajou library

TODO:
    Module Documentation
"""


from __future__ import annotations
from typing import Callable, Iterable


class KinkajouClass:
    """Base Abstract Class for other kinkajou Classes"""


class DataCage(KinkajouClass):
    """DataCage object

    TODO:
        DataCage Documentation
    """

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
        """Return iterable object of headers"""
        return (x for x in self._header)

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
        self._header = newheader

    def column(self: DataCage, column: int | str = 0) -> Iterable:
        """Return iterable object containing all values from a column

        Args:
            column (int | str): either index or header of column to fetch

        Returns:
            iterable: iterable generator of values from column
        """
        if isinstance(column, str):
            column = self._header.index(column)

        return (row[column] for row in self._data)

    def modify_column(self: DataCage, column: int | str, operation: Callable) -> None:
        """Modify a column in the datacage through provided Lambda function

        Args:
            Column (int | str): either index or header of column to modify
            operation (Callable): lambda function to map to column
        """
        if isinstance(column, str):
            column = self._header.index(column)

        # get an interable of our column values
        original_data = self.column(column)

        # map our existing values with the provided callable
        working_data = map(operation, original_data)

        # replace our old values with our new modified values
        for index, value in enumerate(working_data):
            self._data[index][column] = value

    def head(self: DataCage, rows: int = 5) -> None:
        """Print the first <rows> from your datacage

        Args:
            rows (int, optional): Number of Rows(lists) to print. Defaults to 5.
        """
        print(self._header)
        for row in self._data[:rows]:
            print(row)

    def tail(self: DataCage, rows: int = 5) -> None:
        """Print the last <rows> from your datacage

        Args:
            rows (int, optional): Number of Rows(lists) to print. Defaults to 5.
        """
        print(self._header)
        for row in self._data[-rows:]:
            print(row)
